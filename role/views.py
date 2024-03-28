from django.db import transaction, IntegrityError
from django.db.models import ProtectedError
from django.http import JsonResponse
from django.shortcuts import redirect
from .models import Role
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils import timezone
from django.urls import reverse_lazy


# Role CRUD
class RoleListView(LoginRequiredMixin, ListView):
    permission_required = "role.view_role"
    model = Role


class RoleCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "role.add_role"
    model = Role
    fields = ["code", "name", "ad_group_name"]
    success_url = reverse_lazy("role:role_list")
    error_url = reverse_lazy("role:role_create")
    success_message = "Record was created successfully"
    error_message = ("A role with the same combination of name and AD Group already exists. Please enter a unique "
                     "combination.")

    def form_valid(self, form):
        try:
            form.instance.created_by = self.request.user
            return super().form_valid(form)
        except IntegrityError:
            form.add_error(None, "Combination of the name and AD Group should be unique.")
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return redirect(self.error_url)


class RoleUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = "role.change_role"
    model = Role
    fields = ["code", "name", "ad_group_name"]
    success_url = reverse_lazy("role:role_list")
    success_message = "Record was updated successfully"

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class RoleDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = "role.delete_role"
    model = Role
    success_url = reverse_lazy("role:role_list")
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
            messages.error(self.request,
                           "Cannot delete this record because it is referenced to the table of Role Collection Access.")
        return redirect(success_url)


class RoleBulkDeleteView(LoginRequiredMixin, DeleteView):
    """Delete multiple Role"""

    permission_required = "role.delete_role"
    model = Role
    success_url = reverse_lazy("role:role_list")
    success_message = "Records were deleted successfully"
    error_message = "Cannot delete this record because it is referenced to the table of Role Collection Access."

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
