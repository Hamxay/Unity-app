from django.shortcuts import redirect
from django import forms
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.utils import timezone
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from historyconfiguration.helper import history_enable
from .models import Schedule


class RestoreHistoricalVersionForm(forms.Form):
    historical_version = forms.ModelChoiceField(
        queryset=None,
        widget=forms.RadioSelect,
        empty_label=None,
        label="Select a historical version to restore",
    )

    def __init__(self, *args, **kwargs):
        schedule_pk = kwargs.pop("schedule_pk")
        super().__init__(*args, **kwargs)
        self.fields["historical_version"].queryset = Schedule.history.filter(
            pk=schedule_pk
        )


class ScheduleListView(LoginRequiredMixin, ListView):
    """Show the list Schedule"""

    permission_required = "schedule.view_schedule"
    model = Schedule
    paginate_by = 10


class ScheduleCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add Schedule"""

    permission_required = "schedule.add_schedule"
    model = Schedule
    fields = [
        "Code",
        "Name",
        "Frequency",
        "FrequencyInterval",
        "FrequencyRelativeInterval",
        "FrequencyRecurrenceFactor",
        "FrequencySubDayType",
        "FrequencySubDayInterval",
        "ActiveStartDate",
        "ActiveEndDate",
        "ActiveStartTime",
        "ActiveEndTime",
        "IsEnabled",
        "Version",
    ]
    success_url = reverse_lazy("schedule:schedule_list")
    success_message = "Schedule was added successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ScheduleUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update Schedule"""

    permission_required = "schedule.change_schedule"
    model = Schedule
    fields = [
        "Code",
        "Name",
        "Frequency",
        "FrequencyInterval",
        "FrequencyRelativeInterval",
        "FrequencyRecurrenceFactor",
        "FrequencySubDayType",
        "FrequencySubDayInterval",
        "ActiveStartDate",
        "ActiveEndDate",
        "ActiveStartTime",
        "ActiveEndTime",
        "IsEnabled",
        "Version",
    ]
    success_url = reverse_lazy("schedule:schedule_list")
    success_message = "Schedule was updated successfully"

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class ScheduleDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete the Schedule"""

    permission_required = "schedule.delete_schedule"
    model = Schedule
    success_url = reverse_lazy("schedule:schedule_list")
    success_message = "Record was deleted successfully"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.deleted_by = self.request.user
        self.object.deleted_date = timezone.now()
        self.object.delete()
        success_url = self.get_success_url()
        messages.success(self.request, self.success_message)
        return redirect(success_url)


class HistoricalScheduleListView(ListView):
    permission_required = "Schedule.view_schedule"
    template_name = "schedule/historicalschedule_list.html"
    model = Schedule

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.kwargs.get("pk")
        return context


class HistoricalScheduleUpdateView(LoginRequiredMixin, UpdateView):
    model = Schedule.history.model

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        # self.object = self.get_object()
        # selected_version = request.POST.get("historical_version")
        data = Schedule.history.get(pk=pk)
        Schedule_obj = Schedule.objects.get(pk=data.id)
        for field in Schedule_obj._meta.fields:
            field_name = field.name
            setattr(Schedule_obj, field_name, getattr(data, field_name))
        Schedule_obj.save_without_historical_record()
        messages.success(self.request, "Table restored successfully")
        return redirect(reverse_lazy("schedule:schedule_list"))
