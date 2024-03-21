from django.db import transaction
from django.db.models import ProtectedError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
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
from .models import Connection


class RestoreHistoricalVersionForm(forms.Form):
    historical_version = forms.ModelChoiceField(
        queryset=None,
        widget=forms.RadioSelect,
        empty_label=None,
        label="Select a historical version to restore",
    )

    def __init__(self, *args, **kwargs):
        connection_pk = kwargs.pop("connection_pk")
        super().__init__(*args, **kwargs)
        self.fields["historical_version"].queryset = Connection.history.filter(
            pk=connection_pk
        )


class ConnectionListView(LoginRequiredMixin, ListView):
    """Show the list Connection"""

    permission_required = "connection.view_attribute"
    model = Connection
    paginate_by = 10


class ConnectionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add Connection"""

    permission_required = "connection.add_class"
    model = Connection
    fields = [
        "name",
        "description",
        "connection_string"
    ]

    success_url = reverse_lazy("connection:connection_list")
    success_message = "Connection was added successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ConnectionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update Connection"""

    permission_required = "connection.change_class"
    model = Connection
    fields = [
        "name",
        "description",
        "connection_string"
    ]
    success_url = reverse_lazy("connection:connection_list")
    success_message = "Connection was updated successfully"

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class ConnectionDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete the Connection"""

    permission_required = "connection.delete_class"
    model = Connection
    success_url = reverse_lazy("connection:connection_list")
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


class ConnectionBulkDeleteView(LoginRequiredMixin, DeleteView):
    """Delete multiple Connections"""

    permission_required = "connection.connection_bulk_delete"
    model = Connection
    success_url = reverse_lazy("connection:connection_list")
    error_message = "Cannot delete one or more records because they are referenced through protected foreign keys."
    success_message = "Selected Connections were deleted successfully"

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
            messages.error(request, self.error_message)
            return JsonResponse({'success': False, 'message': self.error_message}, status=400)


class HistoricalConnectionListView(ListView):
    permission_required = "connection.view_class"
    template_name = "connection/historicalconnection_list.html"
    model = Connection

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.kwargs.get("pk")
        return context


class HistoricalConnectionUpdateView(LoginRequiredMixin, UpdateView):
    model = Connection.history.model

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        data = Connection.history.get(pk=pk)
        connection_obj = Connection.objects.get(pk=data.code)
        for field in connection_obj._meta.fields:
            field_name = field.name
            setattr(connection_obj, field_name, getattr(data, field_name))
        connection_obj.save()
        messages.success(self.request, "Table restored successfully")
        return redirect(reverse_lazy("connection:connection_list"))


class ConnectionDetailView(LoginRequiredMixin, DetailView):
    permission_required = "connection.connection_detail"
    model = Connection