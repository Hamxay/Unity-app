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
    success_message = "Record was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


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
        self.object = self.get_object()
        self.object.deleted_by = request.user
        self.object.deleted_date = timezone.now()
        self.object.delete()
        success_url = self.get_success_url()
        messages.success(self.request, self.success_message)
        return redirect(success_url)
