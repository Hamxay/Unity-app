import csv
import pandas
from django.core.exceptions import ValidationError
from django.db import transaction, IntegrityError
from django.db.models import ProtectedError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django import forms
from django.views import View
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView, DetailView, FormView,
)
from django.utils import timezone
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib import messages

import accounts.models
from interface.models import Interface
from .download_template import generate_class_csv_template
from .forms import ClassForm, ImportFileForm
from .import_class import import_class_from_file
from .models import Class


class RestoreHistoricalVersionForm(forms.Form):
    historical_version = forms.ModelChoiceField(
        queryset=None,
        widget=forms.RadioSelect,
        empty_label=None,
        label="Select a historical version to restore",
    )

    def __init__(self, *args, **kwargs):
        class_pk = kwargs.pop("class_pk")
        super().__init__(*args, **kwargs)
        self.fields["historical_version"].queryset = Class.history.filter(pk=class_pk)


class ClassListView(LoginRequiredMixin, ListView):
    """Show the list Class"""

    permission_required = "class.view_attribute"
    model = Class
    paginate_by = 10


class ClassCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add Class"""
    form_class = ClassForm
    permission_required = "class.add_class"
    model = Class
    success_url = reverse_lazy("class:class_list")
    success_message = "Class was added successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ClassUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update Class"""

    permission_required = "class.change_class"
    model = Class
    form_class = ClassForm
    success_url = reverse_lazy("class:class_list")
    success_message = "Class was updated successfully"

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class ClassDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete the Class"""

    permission_required = "class.delete_class"
    model = Class
    success_url = reverse_lazy("class:class_list")
    success_message = "Record was deleted successfully"

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            self.object.deleted_by = request.user
            self.object.deleted_date = timezone.now()
            success_url = self.get_success_url()
            self.object.delete()
            messages.success(self.request, self.success_message)
        except ProtectedError as e:
            messages.error(self.request, "Cannot delete this record because it is referenced through protected foreign keys.")
        return redirect(success_url)


class HistoricalClassListView(ListView):
    permission_required = "class.view_class"
    template_name = "classapp/historicalclass_list.html"
    model = Class

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.kwargs.get("pk")
        return context


class HistoricalClassUpdateView(LoginRequiredMixin, UpdateView):
    model = Class.history.model

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        # self.object = self.get_object()
        # selected_version = request.POST.get("historical_version")
        data = Class.history.get(pk=pk)
        class_obj = Class.objects.get(pk=data.Code)

        for field in class_obj._meta.fields:
            field_name = field.name
            setattr(class_obj, field_name, getattr(data, field_name))
        class_obj.save()
        messages.success(self.request, "Table restored successfully")
        return redirect(reverse_lazy("class:class_list"))


class ClassDropdownView(
    LoginRequiredMixin, SuccessMessageMixin, CreateView
):
    success_url = reverse_lazy("class:references")
    success_message = "Class related data requested successfully"

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, Code=self.kwargs[self.slug_url_kwarg])

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.user = request.user
        success_url = self.get_success_url()
        return redirect(success_url)


class ClassDetailView(LoginRequiredMixin, DetailView):
    permission_required = "class.detail"
    model = Class


class DownloadTemplateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return generate_class_csv_template()


class ImportClassFromFileView(LoginRequiredMixin, FormView):
    form_class = ImportFileForm
    success_url = reverse_lazy("class:class_list")

    def form_valid(self, form):
        file = self.request.FILES['file']
        current_user = self.request.user

        import_class_from_file(file, current_user, self.success_url, self.request)

        return redirect(self.get_success_url())


class ClassBulkDeleteView(LoginRequiredMixin, DeleteView):
    """Delete multiple Classes"""

    permission_required = "class.class_bulk_delete"
    model = Class
    success_url = reverse_lazy("class:class_list")
    success_message = "Selected classes were deleted successfully."
    error_message = "Cannot delete one or more records because they are referenced through protected foreign keys."

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
                response = {'success': True, 'message': self.success_message}
        except ProtectedError:
            messages.error(request, self.error_message)
            response = {'success': False, 'message': self.error_message}
        except IntegrityError:
            messages.error(request, "An error occurred while deleting records.")
            response = {'success': False, 'message': "An error occurred while deleting records."}
        return JsonResponse(response)
