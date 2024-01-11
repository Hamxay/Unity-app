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
from .models import Report


# Create your views here.
class ReportListView(LoginRequiredMixin, ListView):
    """Show the list Report"""

    permission_required = "report.view_report"
    model = Report
    paginate_by = 10


class ReportCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add Report"""

    permission_required = "report.add_report"
    model = Report
    fields = "__all__"
    success_url = reverse_lazy("report:report_list")
    success_message = "%(name)s was added successfully"


class ReportUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update Report"""

    permission_required = "report.change_report"
    model = Report
    fields = "__all__"
    success_url = reverse_lazy("report:report_list")
    success_message = "%(name)s was updated successfully"


class ReportDetailView(LoginRequiredMixin, DetailView):
    """Detail view for Report"""

    permission_required = "report.view_report"
    model = Report


class ReportDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete the Report"""

    permission_required = "report.delete_report"
    model = Report
    success_url = reverse_lazy("report:report_list")
    success_message = "Record was deleted successfully"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, self.success_message)
        return redirect(success_url)
