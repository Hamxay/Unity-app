from django.db import transaction
from django.db.models import ProtectedError
from django.http import JsonResponse
from django.shortcuts import redirect, render
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
    error_url = reverse_lazy("collection:collection_create")
    error_message = ("A collection name should be unique in the scope of interface."
                     " Please enter a unique name.")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return render(request=self.request, template_name='collection/collection_form.html', context={'form': form})
    

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
            messages.error(self.request,
                           "Cannot delete this record because it is referenced to the table of Task and Role Collection Access.")
        return redirect(success_url)


class CollectionBulkDeleteView(LoginRequiredMixin, DeleteView):
    """Delete multiple Collections"""

    permission_required = "collection.collection_bulk_delete"
    model = Collection
    success_url = reverse_lazy("collection:collection_list")
    success_message = "Selected collections were deleted successfully."
    error_message = "Cannot delete this record because it is referenced to the tables of Task and Role Collection Access."

    def get(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                records = []
                values = request.GET
                for key, value in values.items():
                    records = [int(num.strip('"')) for num in key.strip('[]').split(',')]
                queryset = self.model.objects.filter(pk__in=records)
                queryset.delete()
                messages.success(request, self.success_message)
                return JsonResponse({'success': True, 'message': self.success_message})
        except ProtectedError:
            messages.error( request, self.error_message)
            return JsonResponse({'success': False, 'message': self.error_message}, status=400)



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
        collection_obj.save()
        messages.success(self.request, "Table restored successfully")
        return redirect(reverse_lazy("collection:collection_list"))


class CollectionDetailView(LoginRequiredMixin, DetailView):
    permission_required = "collection.collection_relations"
    model = Collection
