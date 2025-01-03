from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.db.models import ProtectedError
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import RoleCollectionAccessForm
from .models import RoleCollectionAccess


# RoleCollectionAccess CRUD
class RoleCollectionAccessListView(LoginRequiredMixin, ListView):
    permission_required = 'rolecollectionaccess.view_rolecollectionaccess'
    model = RoleCollectionAccess


class RoleCollectionAccessCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "rolecollectionaccess.add_rolecollectionaccess"
    model = RoleCollectionAccess
    form_class = RoleCollectionAccessForm
    success_url = reverse_lazy("rolecollectionaccess:rolecollectionaccess_list")
    success_message = "Record was created successfully"
    error_url = reverse_lazy("rolecollectionaccess:rolecollectionaccess_create")
    error_message = ("A role collection access with the same combination of collection and role already exists. "
                     "Please enter a unique  combination.")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return render(request=self.request, template_name='rolecollectionaccess/rolecollectionaccess_form.html', context={'form': form})



class RoleCollectionAccessUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = "rolecollectionaccess.change_rolecollectionaccess"
    model = RoleCollectionAccess
    fields = ["code", "collectionId", "RoleId"]
    success_url = reverse_lazy("rolecollectionaccess:rolecollectionaccess_list")
    success_message = "Record was updated successfully"

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class RoleCollectionAccessDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = "rolecollectionaccess.delete_rolecollectionaccess"
    model = RoleCollectionAccess
    success_url = reverse_lazy("rolecollectionaccess:rolecollectionaccess_list")
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


class RoleCollectionAccessBulkDeleteView(LoginRequiredMixin, DeleteView):
    """Delete multiple Role"""

    permission_required = "rolecollectionaccess.delete_rolecollectionaccess"
    model = RoleCollectionAccess
    success_url = reverse_lazy("rolecollectionaccess:rolecollectionaccess_list")
    success_message = "Records were deleted successfully"
    error_message = "Cannot delete one or more collections because they are referenced through protected foreign keys."

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
