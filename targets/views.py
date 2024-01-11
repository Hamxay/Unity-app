from django.shortcuts import redirect
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Targets


class TargetsListView(LoginRequiredMixin, ListView):
    """Show the list Targets"""

    permission_required = "targets.view_targets"
    model = Targets
    paginate_by = 10


class TargetsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add Targets"""

    permission_required = "targets.add_targets"
    model = Targets
    fields = "__all__"
    success_url = reverse_lazy("targets:targets_list")
    success_message = "Record was added successfully"


class TargetsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update Targets"""

    permission_required = "targets.change_targets"
    model = Targets
    fields = "__all__"
    success_url = reverse_lazy("targets:targets_list")
    success_message = "Record was updated successfully"


class TargetsDetailView(LoginRequiredMixin, DetailView):
    """Detail view for Targets"""

    permission_required = "targets.view_targets"
    model = Targets


class TargetsDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete the Targets"""

    permission_required = "targets.delete_targets"
    model = Targets
    success_url = reverse_lazy("targets:targets_list")
    success_message = "Record was deleted successfully"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, self.success_message)
        return redirect(success_url)
