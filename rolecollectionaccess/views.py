from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import RoleCollectionAccessForm
from .models import RoleCollectionAccess


# RoleCollectionAccess CRUD
class RoleCollectionAccessListView(LoginRequiredMixin, ListView):
    permission_required = 'rolecollectionaccess.view_rolecollectionaccess'
    model = RoleCollectionAccess


class RoleCollectionAccessCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "rolecollectionaccess.add_rolecollectionaccess"
    model = RoleCollectionAccess
    form_class = RoleCollectionAccessForm
    success_url = reverse_lazy("rolecollectionaccess:rolecollectionaccess_list")
    success_message = "Record was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class RoleCollectionAccessUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = "rolecollectionaccess.change_rolecollectionaccess"
    model = RoleCollectionAccess
    fields = ["code", "collectionId", "RoleId"]
    success_url = reverse_lazy("rolecollectionaccess:rolecollectionaccess_list")
    success_message = "Record was updated successfully"

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class RoleCollectionAccessDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = "rolecollectionaccess.delete_rolecollectionaccess"
    model = RoleCollectionAccess
    success_url = reverse_lazy("rolecollectionaccess:rolecollectionaccess_list")
    success_message = "Record was deleted successfully"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.deleted_by = request.user
        self.object.deleted_date = timezone.now()
        self.object.delete()
        success_url = self.get_success_url()
        messages.success(self.request, self.success_message)
        return redirect(success_url)
