from django.db import transaction
from django.db.models import ProtectedError
from django.http import JsonResponse
from django.shortcuts import redirect
from .models import StatusProcess as StatusUpcoming
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils import timezone
from django.urls import reverse_lazy


# RoleCollectionAccess CRUD
class StatusUpcomingListView(LoginRequiredMixin, ListView):
    permission_required = 'processstatus.view_processstatus'
    model = StatusUpcoming


class StatusUpcomingCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "processstatus.add_processstatus"
    model = StatusUpcoming
    fields = ["code", "name", "description"]
    success_url = reverse_lazy("processstatus:processstatus_list")
    success_message = "Record was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class StatusUpcomingUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = "processstatus.change_processstatus"
    model = StatusUpcoming
    fields = ["code", "name", "description"]
    success_url = reverse_lazy("processstatus:processstatus_list")
    success_message = "Record was updated successfully"

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class StatusUpcomingDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = "processstatus.delete_processstatus"
    model = StatusUpcoming
    success_url = reverse_lazy("processstatus:processstatus_list")
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

    permission_required = "processstatus.delete_processstatus"
    model = StatusUpcoming
    success_url = reverse_lazy("processstatus:processstatus_list")
    success_message = "Records were deleted successfully"
    error_message = "Cannot delete one or more collections because they are referenced through protected foreign keys."

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
            messages.error(self.request, self.error_message)
            return JsonResponse({'success': False, 'message': self.error_message}, status=400)

