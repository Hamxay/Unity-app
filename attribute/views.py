from django.shortcuts import redirect
from django import forms
from django.views import View
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView, FormView,
)
from django.utils import timezone
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import AttributeForm, ImportFileForm
from .import_attribute import import_attributes_from_file
from .models import Attribute
from .download_template import AttributeTemplateCSVGenerator


class RestoreHistoricalVersionForm(forms.Form):
    historical_version = forms.ModelChoiceField(
        queryset=None,
        widget=forms.RadioSelect,
        empty_label=None,
        label="Select a historical version to restore",
    )

    def __init__(self, *args, **kwargs):
        attribute_pk = kwargs.pop("attribute_pk")
        super().__init__(*args, **kwargs)
        self.fields["historical_version"].queryset = Attribute.history.filter(
            pk=attribute_pk
        )


class AttributeListView(LoginRequiredMixin, ListView):
    """Show the list Attribute"""

    permission_required = "attribute.view_attribute"
    model = Attribute
    paginate_by = 10


class AttributeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add Attribute"""
    form_class = AttributeForm
    permission_required = "attribute.add_attribute"
    model = Attribute
    success_url = reverse_lazy("attribute:attribute_list")
    success_message = "Attribute was added successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AttributeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update Attribute"""

    permission_required = "attribute.change_attribute"
    model = Attribute
    form_class = AttributeForm
    success_url = reverse_lazy("attribute:attribute_list")
    success_message = "Attribute was updated successfully"

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class AttributeDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete the Attribute"""

    permission_required = "attribute.delete_attribute"
    model = Attribute
    success_url = reverse_lazy("attribute:attribute_list")
    success_message = "Record was deleted successfully"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.deleted_by = self.request.user
        self.object.deleted_date = timezone.now()
        self.object.delete()
        success_url = self.get_success_url()
        messages.success(self.request, self.success_message)
        return redirect(success_url)


class HistoricalAttributeListView(ListView):
    permission_required = "attribute.view_attribute"
    template_name = "attribute/historicalattribute_list.html"
    model = Attribute

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.kwargs.get("pk")
        return context


class HistoricalAttributeUpdateView(LoginRequiredMixin, UpdateView):
    model = Attribute.history.model

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        # self.object = self.get_object()
        # selected_version = request.POST.get("historical_version")
        data = Attribute.history.get(pk=pk)
        attribute_obj = Attribute.objects.get(pk=data.id)
        for field in attribute_obj._meta.fields:
            field_name = field.name
            setattr(attribute_obj, field_name, getattr(data, field_name))
        attribute_obj.save_without_historical_record()
        messages.success(self.request, "Table restored successfully")
        return redirect(reverse_lazy("attribute:attribute_list"))


class AttributeDownloadTemplateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        response = AttributeTemplateCSVGenerator.generate_csv()
        return response


class AttributeImportClassFromFileView(LoginRequiredMixin, FormView):
    form_class = ImportFileForm
    success_url = reverse_lazy("attribute:attribute_list")

    def form_valid(self, form):
        file = self.request.FILES['file']
        current_user = self.request.user

        import_attributes_from_file(file, current_user, self.success_url, self.request)

        return redirect(self.get_success_url())
