from django.shortcuts import redirect
from .models import LoadPattern
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils import timezone
from django.urls import reverse_lazy

# LoadPattern CRUD


class LoadPatternListView(LoginRequiredMixin, ListView):
    permission_required = "pattern.view_loadpattern"
    model = LoadPattern


class LoadPatternCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "pattern.add_loadpattern"
    model = LoadPattern
    fields = ["code", "name", "description"]
    success_url = reverse_lazy("pattern:load_pattern_list")
    success_message = "Record was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class LoadPatternUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = "pattern.change_loadpattern"
    model = LoadPattern
    fields = ["code", "name", "description"]
    success_url = reverse_lazy("pattern:load_pattern_list")
    success_message = "Record was updated successfully"

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class LoadPatternDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = "pattern.delete_loadpattern"
    model = LoadPattern
    template_name = "pattern/pattern_confirm_delete.html"
    success_url = reverse_lazy("pattern:load_pattern_list")
    success_message = "Record was deleted successfully"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.deleted_by = request.user
        self.object.deleted_date = timezone.now()
        self.object.delete()
        success_url = self.get_success_url()
        messages.success(self.request, self.success_message)
        return redirect(success_url)


class LoadPatternDetailView(LoginRequiredMixin, DetailView):
    permission_required = "pattern.detail"
    model = LoadPattern
