from django.db import transaction
from django.db.models import ProtectedError
from django.shortcuts import redirect
from .models import StatusUpcoming
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils import timezone
from django.urls import reverse_lazy


# RoleCollectionAccess CRUD
class StatusUpcomingListView(LoginRequiredMixin, ListView):
    permission_required = 'statusupcoming.view_statusupcoming'
    model = StatusUpcoming


class StatusUpcomingCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "statusupcoming.add_statusupcoming"
    model = StatusUpcoming
    fields = ["code", "name", "description"]
    success_url = reverse_lazy("statusupcoming:statusupcoming_list")
    success_message = "Record was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class StatusUpcomingUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = "statusupcoming.change_statusupcoming"
    model = StatusUpcoming
    fields = ["code", "name", "description"]
    success_url = reverse_lazy("statusupcoming:statusupcoming_list")
    success_message = "Record was updated successfully"

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class StatusUpcomingDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = "statusupcoming.delete_statusupcoming"
    model = StatusUpcoming
    success_url = reverse_lazy("statusupcoming:statusupcoming_list")
    success_message = "Record was deleted successfully"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.deleted_by = request.user
        self.object.deleted_date = timezone.now()
        self.object.delete()
        success_url = self.get_success_url()
        messages.success(self.request, self.success_message)
        return redirect(success_url)



class StatusUpcomingBulkDeleteView(LoginRequiredMixin, DeleteView):
    """Delete multiple StatusUpcoming"""

    permission_required = "statusupcoming.statusupcoming_bulk_delete"
    model = StatusUpcoming
    success_url = reverse_lazy("statusupcoming:statusupcoming_list")
    success_message = "Records were deleted successfully"

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
        except ProtectedError:
            messages.error(self.request, "Cannot delete one or more records because they are referenced through protected foreign keys.")

        return redirect(self.success_url)

