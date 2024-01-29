from django.shortcuts import redirect, get_object_or_404
from django import forms
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,

)
from django.utils import timezone
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import InterfaceCategory, InterfaceType, Interface, InterfaceDependence
from .forms import InterfaceForm, InterfaceDependenceForm


# InterfaceCategory CRUD
class InterfaceCategoryListView(LoginRequiredMixin, ListView):
    permission_required = "interface.view_interfacecategory"
    model = InterfaceCategory


class InterfaceCategoryDetailView(LoginRequiredMixin, DetailView):
    permission_required = "interface.detail_interfacecategory"
    model = InterfaceCategory


class InterfaceDetailView(LoginRequiredMixin, DetailView):
    permission_required = "interface.detail"
    model = Interface


class InterfaceCategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "interface.add_interfacecategory"
    model = InterfaceCategory
    fields = ["name", "description"]
    success_url = reverse_lazy("interface:interface_category_list")
    success_message = "Record was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class InterfaceCategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = "interface.change_interfacecategory"
    model = InterfaceCategory
    fields = ["name", "description"]
    success_url = reverse_lazy("interface:interface_category_list")
    success_message = "Record was updated successfully"
    slug_url_kwarg = 'code'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
    def get_object(self, queryset=None):
        return get_object_or_404(self.model, code=self.kwargs[self.slug_url_kwarg])


class InterfaceCategoryDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = "interface.delete_interfacecategory"
    model = InterfaceCategory
    template_name = "interface/interface_category_confirm_delete.html"
    success_url = reverse_lazy("interface:interface_category_list")
    success_message = "Record was deleted successfully"
    slug_url_kwarg = 'code'
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.deleted_by = request.user
        self.object.deleted_date = timezone.now()
        self.object.delete()
        success_url = self.get_success_url()
        messages.success(self.request, self.success_message)
        return redirect(success_url)
    def get_object(self, queryset=None):
        return get_object_or_404(self.model, code=self.kwargs[self.slug_url_kwarg])


# InterfaceType CRUD
class InterfaceTypeListView(LoginRequiredMixin, ListView):
    permission_required = "interface.view_interfacetype"
    model = InterfaceType


class InterfaceTypeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "interface.add_interfacetype"
    model = InterfaceType
    fields = ["name", "description"]
    success_url = reverse_lazy("interface:interface_type_list")
    success_message = "Record was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class InterfaceTypeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = "interface.change_interfacetype"
    model = InterfaceType
    fields = [ "name", "description"]
    success_url = reverse_lazy("interface:interface_type_list")
    success_message = "Record was updated successfully"
    slug_url_kwarg = 'code'
    
    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
    
    def get_object(self, queryset=None):
        return get_object_or_404(self.model, code=self.kwargs[self.slug_url_kwarg])


class InterfaceTypeDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = "interface.delete_interfacetype"
    model = InterfaceType
    success_url = reverse_lazy("interface:interface_type_list")
    success_message = "Record was deleted successfully"
    slug_url_kwarg = 'code'
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.deleted_by = request.user
        self.object.deleted_date = timezone.now()
        self.object.delete()
        success_url = self.get_success_url()
        messages.success(self.request, self.success_message)
        return redirect(success_url)
    def get_object(self, queryset=None):
        return get_object_or_404(self.model, code=self.kwargs[self.slug_url_kwarg])


class InterfaceTypeDetailView(LoginRequiredMixin, DetailView):
    permission_required = "interface.interfacetype_detail"
    model = InterfaceType


class RestoreHistoricalVersionForm(forms.Form):
    historical_version = forms.ModelChoiceField(
        queryset=None,
        widget=forms.RadioSelect,
        empty_label=None,
        label="Select a historical version to restore",
    )

    def __init__(self, *args, **kwargs):
        interface_pk = kwargs.pop("interface_pk")
        super().__init__(*args, **kwargs)
        self.fields["historical_version"].queryset = Interface.history.filter(
            pk=interface_pk
        )


class InterfaceListView(LoginRequiredMixin, ListView):
    """Show the list Interface"""

    permission_required = "interface.view_attribute"
    model = Interface
    paginate_by = 10


class InterfaceCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add Interface"""

    permission_required = "interface.add_class"
    form_class = InterfaceForm
    model = Interface

    success_url = reverse_lazy("interface:interface_list")
    success_message = "Interface was added successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class InterfaceUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update Interface"""

    permission_required = "interface.change_class"
    model = Interface
    slug_url_kwarg = 'code'
    fields = [
        "interface_category_id",
        "interface_type_id",
        "schedule_id",
        "connection_id",
        "name",
        "description",
        "priority",
        "max_concurrent_sessions",
        "run_window",
        "is_enabled",
        "active_start_date",
        "active_end_date",
        "retry_times",
        "wait_action",
    ]
    success_url = reverse_lazy("interface:interface_list")
    success_message = "Interface was updated successfully"

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
    def get_object(self, queryset=None):
        return get_object_or_404(self.model, code=self.kwargs[self.slug_url_kwarg])


class InterfaceDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete the Interface"""

    permission_required = "interface.delete_class"
    model = Interface
    success_url = reverse_lazy("interface:interface_list")
    success_message = "Record was deleted successfully"
    slug_url_kwarg = 'code'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.deleted_by = request.user
        self.object.deleted_date = timezone.now()
        self.object.delete()
        success_url = self.get_success_url()
        messages.success(self.request, self.success_message)
        return redirect(success_url)

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, code=self.kwargs[self.slug_url_kwarg])


class HistoricalInterfaceListView(ListView):
    permission_required = "interface.view_class"
    template_name = "interface/historicalinterface_list.html"
    model = Interface

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.kwargs.get("pk")
        return context


class HistoricalInterfaceUpdateView(LoginRequiredMixin, UpdateView):
    model = Interface.history.model

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        data = Interface.history.get(pk=pk)
        interface_obj = Interface.objects.get(pk=data.id)
        for field in interface_obj._meta.fields:
            field_name = field.name
            setattr(interface_obj, field_name, getattr(data, field_name))
        interface_obj.save_without_historical_record()
        messages.success(self.request, "Table restored successfully")
        return redirect(reverse_lazy("interface:interface_list"))


# InterfaceDependence CRUD
class InterfaceDependenceListView(LoginRequiredMixin, ListView):
    permission_required = "interface.view_dependence"
    model = InterfaceDependence


class InterfaceDependenceCreateView(
    LoginRequiredMixin, SuccessMessageMixin, CreateView
):
    permission_required = "interface.add_dependence"
    model = InterfaceDependence
    form_class = InterfaceDependenceForm
    success_url = reverse_lazy("interface:interface_dependence_list")
    success_message = "Record was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class InterfaceDependenceUpdateView(
    LoginRequiredMixin, SuccessMessageMixin, UpdateView
):
    permission_required = "interface.change_dependence"
    model = InterfaceDependence
    fields = ["interface_id", "dependent_on_interface"]
    success_url = reverse_lazy("interface:interface_dependence_list")
    success_message = "Record was updated successfully"
    slug_url_kwarg = 'code'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
    def get_object(self, queryset=None):
        return get_object_or_404(self.model, code=self.kwargs[self.slug_url_kwarg])



class InterfaceDependenceDeleteView(
    LoginRequiredMixin, SuccessMessageMixin, DeleteView
):
    permission_required = "interface.delete_dependence"
    model = InterfaceDependence
    success_url = reverse_lazy("interface:interface_dependence_list")
    success_message = "Record was deleted successfully"
    slug_url_kwarg = 'code'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.deleted_by = request.user
        self.object.deleted_date = timezone.now()
        self.object.delete()
        success_url = self.get_success_url()
        messages.success(self.request, self.success_message)
        return redirect(success_url)


class InterfaceDropdownView(
    LoginRequiredMixin, SuccessMessageMixin, CreateView

):
    success_url = reverse_lazy("interface:references")
    success_message = "Related data requested successfully"

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, code=self.kwargs[self.slug_url_kwarg])

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.user = request.user
        success_url = self.get_success_url()
        return redirect(success_url)


   

