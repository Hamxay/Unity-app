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
from .models import Entity


class EntityListView(LoginRequiredMixin, ListView):
    """Show the list Entity"""

    permission_required = "entity.view_entity"
    model = Entity
    paginate_by = 10


class EntityCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add Entity"""

    permission_required = "entity.add_entity"
    model = Entity
    fields = "__all__"
    success_url = reverse_lazy("entity:entity_list")
    success_message = "%(name)s was added successfully"


class EntityUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update Entity"""

    permission_required = "entity.change_entity"
    model = Entity
    fields = "__all__"
    success_url = reverse_lazy("entity:entity_list")
    success_message = "%(name)s was updated successfully"


class EntityDetailView(LoginRequiredMixin, DetailView):
    """Detail view for Entity"""

    permission_required = "entity.view_entity"
    model = Entity


class EntityDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete the Entity"""

    permission_required = "entity.delete_entity"
    model = Entity
    success_url = reverse_lazy("entity:entity_list")
    success_message = "Record was deleted successfully"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, self.success_message)
        return redirect(success_url)
