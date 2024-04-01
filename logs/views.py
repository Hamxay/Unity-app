from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import APIIngestionBatchStatusLog,CheckpointLog,AuditLog, RunLog, RunStepLog


# Create your views here.
class APIIngestionBatchStatusLogListView(LoginRequiredMixin, ListView):
    """Show the list APIIngestionBatchStatusLog"""

    permission_required = "logs.view_APIIngestionBatchStatusLog"
    model = APIIngestionBatchStatusLog
    paginate_by = 10


class APIIngestionBatchStatusLogDetailView(LoginRequiredMixin, DetailView):
    """Show the Details APIIngestionBatchStatusLog"""

    permission_required = "logs.view_APIIngestionBatchStatusLog"
    model = APIIngestionBatchStatusLog

class CheckpointLogListView(LoginRequiredMixin, ListView):
    """Show the list CheckpointLog"""

    permission_required = "logs.view_CheckpointLog"
    model = CheckpointLog
    paginate_by = 10


class AuditLogListView(LoginRequiredMixin, ListView):
    """Show the list AuditLog"""

    permission_required = "logs.AuditLog"
    model = AuditLog
    paginate_by = 10


class RunLogListView(LoginRequiredMixin, ListView):
    """Show the list AuditLog"""

    permission_required = "logs.view_RunLog"
    model = RunLog
    paginate_by = 10


class RunStepLogListView(LoginRequiredMixin, ListView):
    """Show the list AuditLog"""

    permission_required = "logs.view_RunStepLog"
    model = RunStepLog
    paginate_by = 10
