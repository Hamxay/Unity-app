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
from .models import StatusGroup, Status, StatusCriteria


# Status Views
class StatusListView(LoginRequiredMixin, ListView):
    """Show the list Status"""

    permission_required = "status.view_status"
    model = Status
    paginate_by = 10


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add Status"""

    permission_required = "status.add_status"
    model = Status
    fields = "__all__"
    success_url = reverse_lazy("status:status_list")
    success_message = "%(name)s was added successfully"


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update Status"""

    permission_required = "status.change_status"
    model = Status
    fields = "__all__"
    success_url = reverse_lazy("status:status_list")
    success_message = "%(name)s was updated successfully"


class StatusDetailView(LoginRequiredMixin, DetailView):
    """Detail view for Status"""

    permission_required = "status.view_status"
    model = Status


class StatusDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete the Status"""

    permission_required = "status.delete_status"
    model = Status
    success_url = reverse_lazy("status:status_list")
    success_message = "Record was deleted successfully"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, self.success_message)
        return redirect(success_url)


# StatusCriteria Views
class StatusCriteriaListView(LoginRequiredMixin, ListView):
    """Show the list StatusCriteria"""

    permission_required = "status.view_statuscriteria"
    model = StatusCriteria
    paginate_by = 10


class StatusCriteriaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add StatusCriteria"""

    permission_required = "status.add_statuscriteria"
    model = StatusCriteria
    fields = "__all__"
    success_url = reverse_lazy("status:status_criteria_list")
    success_message = "Record was added successfully"


class StatusCriteriaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update StatusCriteria"""

    permission_required = "status.change_statuscriteria"
    model = StatusCriteria
    fields = "__all__"
    success_url = reverse_lazy("status:status_criteria_list")
    success_message = "Record was updated successfully"


class StatusCriteriaDetailView(LoginRequiredMixin, DetailView):
    """Detail view for StatusCriteria"""

    permission_required = "status.view_statuscriteria"
    model = StatusCriteria


class StatusCriteriaDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete the StatusCriteria"""

    permission_required = "status.delete_statuscriteria"
    model = StatusCriteria
    success_url = reverse_lazy("status:status_criteria_list")
    success_message = "Record was deleted successfully"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, self.success_message)
        return redirect(success_url)


# StatusGroup Views
class StatusGroupListView(LoginRequiredMixin, ListView):
    """Show the list StatusGroup"""

    permission_required = "status.view_statusgroup"
    model = StatusGroup
    paginate_by = 10


class StatusGroupCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add StatusGroup"""

    permission_required = "status.add_statusgroup"
    model = StatusGroup
    fields = "__all__"
    success_url = reverse_lazy("status:status_group_list")
    success_message = "%(name)s was added successfully"


class StatusGroupUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update StatusGroup"""

    permission_required = "status.change_statusgroup"
    model = StatusGroup
    fields = "__all__"
    success_url = reverse_lazy("status:status_group_list")
    success_message = "%(name)s was updated successfully"


class StatusGroupDetailView(LoginRequiredMixin, DetailView):
    """Detail view for StatusGroup"""

    permission_required = "status.view_statusgroup"
    model = StatusGroup


class StatusGroupDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete the StatusGroup"""

    permission_required = "status.delete_statusgroup"
    model = StatusGroup
    success_url = reverse_lazy("status:status_group_list")
    success_message = "Record was deleted successfully"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, self.success_message)
        return redirect(success_url)
