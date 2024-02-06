from django.db.models import ProtectedError
from django.shortcuts import redirect
from django import forms
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView, DetailView,
)
from django.utils import timezone
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import CollectionForm
from .models import Collection


class RestoreHistoricalVersionForm(forms.Form):
    historical_version = forms.ModelChoiceField(
        queryset=None,
        widget=forms.RadioSelect,
        empty_label=None,
        label="Select a historical version to restore",
    )

    def __init__(self, *args, **kwargs):
        collection_pk = kwargs.pop("collection_pk")
        super().__init__(*args, **kwargs)
        self.fields["historical_version"].queryset = Collection.history.filter(
            pk=collection_pk
        )


class CollectionListView(LoginRequiredMixin, ListView):
    """Show the list Collection"""

    permission_required = "collection.view_attribute"
    model = Collection
    paginate_by = 10


class CollectionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add Collection"""

    permission_required = "collection.add_class"
    model = Collection
    form_class = CollectionForm

    success_url = reverse_lazy("collection:collection_list")
    success_message = "Collection was added successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CollectionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update Collection"""

    permission_required = "collection.change_class"
    model = Collection
    fields = [
        "interfaceid",
        "name",
        "description",
        "executionorder",
        "executiontriggerrule",
    ]

    success_url = reverse_lazy("collection:collection_list")
    success_message = "Collection was updated successfully"

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class CollectionDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete the Collection"""

    permission_required = "collection.delete_class"
    model = Collection
    success_url = reverse_lazy("collection:collection_list")
    success_message = "Record was deleted successfully"

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            self.object.deleted_by = request.user
            self.object.deleted_date = timezone.now()
            success_url = self.get_success_url()
            self.object.delete()
            messages.success(self.request, self.success_message)
        except ProtectedError:
            messages.error(self.request, "Cannot delete this record because it is referenced through protected foreign keys.")
        return redirect(success_url)


class HistoricalCollectionListView(ListView):
    permission_required = "collection.view_class"
    template_name = "collection/historicalcollection_list.html"
    model = Collection

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.kwargs.get("pk")
        return context


class HistoricalCollectionUpdateView(LoginRequiredMixin, UpdateView):
    model = Collection.history.model

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        data = Collection.history.get(pk=pk)
        collection_obj = Collection.objects.get(pk=data.code)
        for field in collection_obj._meta.fields:
            field_name = field.name
            setattr(collection_obj, field_name, getattr(data, field_name))
        collection_obj.save_without_historical_record()
        messages.success(self.request, "Table restored successfully")
        return redirect(reverse_lazy("collection:collection_list"))


class CollectionDetailView(LoginRequiredMixin, DetailView):
    permission_required = "collection.collection_relations"
    model = Collection