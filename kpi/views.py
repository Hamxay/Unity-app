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
from .models import KPI, KPIGroup, KPISubGroup


# KPI Views
class KPIListView(LoginRequiredMixin, ListView):
    """Show the list KPI"""

    permission_required = "kpi.view_kpi"
    model = KPI
    paginate_by = 10


class KPICreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add KPI"""

    permission_required = "kpi.add_kpi"
    model = KPI
    fields = "__all__"
    success_url = reverse_lazy("kpi:kpi_list")
    success_message = "%(name)s was added successfully"


class KPIUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update KPI"""

    permission_required = "kpi.change_kpi"
    model = KPI
    fields = "__all__"
    success_url = reverse_lazy("kpi:kpi_list")
    success_message = "%(name)s was updated successfully"


class KPIDetailView(LoginRequiredMixin, DetailView):
    """Detail view for KPI"""

    permission_required = "kpi.view_kpi"
    model = KPI


class KPIDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete the KPI"""

    permission_required = "kpi.delete_kpi"
    model = KPI
    success_url = reverse_lazy("kpi:kpi_list")
    success_message = "Record was deleted successfully"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, self.success_message)
        return redirect(success_url)


# KPIGroup Views
class KPIGroupListView(LoginRequiredMixin, ListView):
    """Show the list KPIGroup"""

    permission_required = "kpi.view_kpigroup"
    model = KPIGroup
    paginate_by = 10


class KPIGroupCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add KPIGroup"""

    permission_required = "kpi.add_kpigroup"
    model = KPIGroup
    fields = "__all__"
    success_url = reverse_lazy("kpi:kpi_group_list")
    success_message = "%(name)s was added successfully"


class KPIGroupUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update KPIGroup"""

    permission_required = "kpi.change_kpigroup"
    model = KPIGroup
    fields = "__all__"
    success_url = reverse_lazy("kpi:kpi_group_list")
    success_message = "%(name)s was updated successfully"


class KPIGroupDetailView(LoginRequiredMixin, DetailView):
    """Detail view for KPIGroup"""

    permission_required = "kpi.view_kpigroup"
    model = KPIGroup


class KPIGroupDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete the KPIGroup"""

    permission_required = "kpi.delete_kpigroup"
    model = KPIGroup
    success_url = reverse_lazy("kpi:kpi_group_list")
    success_message = "Record was deleted successfully"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, self.success_message)
        return redirect(success_url)


# KPISubGroup Views
class KPISubGroupListView(LoginRequiredMixin, ListView):
    """Show the list KPISubGroup"""

    permission_required = "kpi.view_kpisubgroup"
    model = KPISubGroup
    paginate_by = 10


class KPISubGroupCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add KPISubGroup"""

    permission_required = "kpi.add_kpisubgroup"
    model = KPISubGroup
    fields = "__all__"
    success_url = reverse_lazy("kpi:kpi_sub_group_list")
    success_message = "%(name)s was added successfully"


class KPISubGroupUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update KPISubGroup"""

    permission_required = "kpi.change_kpisubgroup"
    model = KPISubGroup
    fields = "__all__"
    success_url = reverse_lazy("kpi:kpi_sub_group_list")
    success_message = "%(name)s was updated successfully"


class KPISubGroupDetailView(LoginRequiredMixin, DetailView):
    """Detail view for KPISubGroup"""

    permission_required = "kpi.view_kpisubgroup"
    model = KPISubGroup


class KPISubGroupDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete the KPISubGroup"""

    permission_required = "kpi.delete_kpisubgroup"
    model = KPISubGroup
    success_url = reverse_lazy("kpi:kpi_sub_group_list")
    success_message = "Record was deleted successfully"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, self.success_message)
        return redirect(success_url)
