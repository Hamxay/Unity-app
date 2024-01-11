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
from .models import Frequency


class FrequencyListView(LoginRequiredMixin, ListView):
    """Show the list Frequency"""

    permission_required = "frequency.view_frequency"
    model = Frequency
    paginate_by = 10


class FrequencyCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add Frequency"""

    permission_required = "frequency.add_frequency"
    model = Frequency
    fields = "__all__"
    success_url = reverse_lazy("frequency:frequency_list")
    success_message = "%(name)s was added successfully"


class FrequencyUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update Frequency"""

    permission_required = "frequency.change_frequency"
    model = Frequency
    fields = "__all__"
    success_url = reverse_lazy("frequency:frequency_list")
    success_message = "%(name)s was updated successfully"


class FrequencyDetailView(LoginRequiredMixin, DetailView):
    """Detail view for Frequency"""

    permission_required = "frequency.view_frequency"
    model = Frequency


class FrequencyDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete the Frequency"""

    permission_required = "frequency.delete_frequency"
    model = Frequency
    success_url = reverse_lazy("frequency:frequency_list")
    success_message = "Record was deleted successfully"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, self.success_message)
        return redirect(success_url)
