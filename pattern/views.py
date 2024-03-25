from django.db import transaction
from django.db.models import ProtectedError
from django.http import JsonResponse
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
        try:
            self.object = self.get_object()
            self.object.deleted_by = request.user
            self.object.deleted_date = timezone.now()
            success_url = self.get_success_url()
            self.object.delete()
            messages.success(self.request, self.success_message)
        except ProtectedError as e:
            messages.error(self.request,
                           "Cannot delete this record because it is referenced to the table of Task.")
        return redirect(success_url)


class LoadPatternBulkDeleteView(LoginRequiredMixin, DeleteView):    
    """Delete multiple Attributes"""

    permission_required = "pattern.pattern_bulk_delete"
    model = LoadPattern
    success_url = reverse_lazy("pattern:load_pattern_list")
    success_message = "Records were deleted successfully"
    error_message = "Cannot delete one or more records because they are referenced to the table of Task."

    def get(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                records = []
                values = request.GET
                for key, value in values.items():
                    records = [int(num.strip('"')) for num in key.strip('[]').split(',')]
                queryset = self.model.objects.filter(pk__in=records)
                queryset.delete()
                messages.success(request, self.success_message)
                return JsonResponse({'success': True, 'message': self.success_message})
        except ProtectedError:
            messages.error(self.request, self.error_message)
            return JsonResponse({'success': False, 'message': self.error_message}, status=400)


class LoadPatternDetailView(LoginRequiredMixin, DetailView):
    permission_required = "pattern.detail"
    model = LoadPattern
