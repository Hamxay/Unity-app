import csv

import pandas
from django.core.exceptions import ValidationError
from django.db.models import ProtectedError
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, redirect
from django import forms
from django.views import View
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView, DetailView, FormView,
)
from django.utils import timezone
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from Task.download_template import generate_task_csv_template
from Task.forms import TaskForm, ImportFileForm
from Task.import_task import import_tasks_from_file
from Task.models import Task
from classapp.models import Class
from collection.models import Collection
from pattern.models import LoadPattern


class RestoreHistoricalVersionForm(forms.Form):
    historical_version = forms.ModelChoiceField(
        queryset=None,
        widget=forms.RadioSelect,
        empty_label=None,
        label="Select a historical version to restore",
    )

    def __init__(self, *args, **kwargs):
        task_pk = kwargs.pop("task_pk")
        super().__init__(*args, **kwargs)
        self.fields["historical_version"].queryset = Task.history.filter(pk=task_pk)


class TaskListView(LoginRequiredMixin, ListView):
    """Show the list Class"""

    permission_required = "Task.view_Task"
    model = Task
    paginate_by = 10


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add Class"""

    permission_required = "Task.add_Task"
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("Task:Task_list")
    success_message = "Task was added successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update Class"""

    permission_required = "Task.change_Task"
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("Task:Task_list")
    success_message = "Task was updated successfully"

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete the Class"""

    permission_required = "Task.delete_Task"
    model = Task
    success_url = reverse_lazy("Task:Task_list")
    success_message = "Record was deleted successfully"

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            self.object.deleted_by = request.user
            self.object.deleted_date = timezone.now()
            success_url = self.get_success_url()
            self.object.delete()
            messages.success(self.request, self.success_message)
        except ProtectedError:
            messages.error(self.request, "Cannot delete this record because it is referenced through protected foreign keys.")
        return redirect(success_url)


class HistoricalTaskListView(ListView):
    permission_required = "class.view_class"
    template_name = "Task/historicaltask_list.html"
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.kwargs.get("pk")
        return context


class HistoricalTaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task.history.model

    def get(self, request, *args, **kwargs):
        history_id = self.kwargs.get("pk")
        historical_record = get_object_or_404(Task.history.model, history_id=history_id)

        if historical_record.history_type == '-':
            # Create a new instance of Class using the historical record's data
            new_task = Task(
                Code=historical_record.Code,
                ClassId=historical_record.ClassId,
                CollectionId=historical_record.CollectionId,
                LoadPatternId=historical_record.LoadPatternId,
                Name=historical_record.Name,
                Description=historical_record.Description,
                ProcessName=historical_record.ProcessName,
                ProcessParameters=historical_record.ProcessParameters,
                SubProcessParameters=historical_record.SubProcessParameters,
                DeduplicateSource=historical_record.DeduplicateSource,
                Priority=historical_record.Priority,
                created_by=historical_record.created_by,
                created_date=historical_record.created_date,
                updated_date=timezone.now(),
                updated_by=request.user
            )
            new_task.save()
            messages.success(request, "New record created successfully")
        else:
            task_obj = Task.objects.get(pk=historical_record.id)

            # Update fields from historical data
            for field in task_obj._meta.fields:
                field_name = field.name
                setattr(task_obj, field_name, getattr(historical_record, field_name))

            task_obj.save()
            messages.success(request, "Record restored successfully")
        return redirect(reverse_lazy("Task:Task_list"))


class HistoricalTaskViewAll(LoginRequiredMixin, ListView):
    permission_required = "Task.view_Task"
    template_name = "Task/historicaltask_list_all.html"
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    permission_required = "Task.detail"
    model = Task


class TaskDownloadTemplateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return generate_task_csv_template()


class TaskImportClassFromFileView(LoginRequiredMixin, FormView):
    form_class = ImportFileForm
    success_url = reverse_lazy("Task:Task_list")

    def form_valid(self, form):
        file = self.request.FILES['file']
        current_user = self.request.user

        import_tasks_from_file(file, current_user, self.success_url, self.request)

        return redirect(self.get_success_url())
