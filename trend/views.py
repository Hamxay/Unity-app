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
from .models import Trend, TrendCriteria


# Trend Views
class TrendListView(LoginRequiredMixin, ListView):
    """Show the list Trend"""

    permission_required = "trend.view_trend"
    model = Trend
    paginate_by = 10


class TrendCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add Trend"""

    permission_required = "trend.add_trend"
    model = Trend
    fields = "__all__"
    success_url = reverse_lazy("trend:trend_list")
    success_message = "%(name)s was added successfully"


class TrendUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update Trend"""

    permission_required = "trend.change_trend"
    model = Trend
    fields = "__all__"
    success_url = reverse_lazy("trend:trend_list")
    success_message = "%(name)s was updated successfully"


class TrendDetailView(LoginRequiredMixin, DetailView):
    """Detail view for Trend"""

    permission_required = "trend.view_trend"
    model = Trend


class TrendDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete the Trend"""

    permission_required = "trend.delete_trend"
    model = Trend
    success_url = reverse_lazy("trend:trend_list")
    success_message = "Record was deleted successfully"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, self.success_message)
        return redirect(success_url)


# TrendCriteria Views
class TrendCriteriaListView(LoginRequiredMixin, ListView):
    """Show the list TrendCriteria"""

    permission_required = "trend.view_trendcriteria"
    model = TrendCriteria
    paginate_by = 10


class TrendCriteriaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add TrendCriteria"""

    permission_required = "trend.add_trendcriteria"
    model = TrendCriteria
    fields = "__all__"
    success_url = reverse_lazy("trend:trend_criteria_list")
    success_message = "Record was added successfully"


class TrendCriteriaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update TrendCriteria"""

    permission_required = "trend.change_trendcriteria"
    model = TrendCriteria
    fields = "__all__"
    success_url = reverse_lazy("trend:trend_criteria_list")
    success_message = "Record was updated successfully"


class TrendCriteriaDetailView(LoginRequiredMixin, DetailView):
    """Detail view for Trend"""

    permission_required = "trend.view_trendcriteria"
    model = TrendCriteria


class TrendCriteriaDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete the TrendCriteria"""

    permission_required = "trend.delete_trendcriteria"
    model = TrendCriteria
    success_url = reverse_lazy("trend:trend_criteria_list")
    success_message = "Record was deleted successfully"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, self.success_message)
        return redirect(success_url)
