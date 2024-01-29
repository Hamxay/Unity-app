from django import forms
from .models import Interface, InterfaceDependence


# from autocomplete_light import shortcuts as al


class InterfaceForm(forms.ModelForm):
    class Meta:
        model = Interface
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
        labels = {
            'interface_category_id': 'Interface Category',
            'interface_type_id': 'Interface Type',
            'schedule_id':'Schedule',
            'connection_id':'Connection',
        }
        widgets = {
            'active_start_date': forms.DateInput(attrs={'type': 'date'}),
            'active_end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class InterfaceDependenceForm(forms.ModelForm):
    class Meta:
        model = InterfaceDependence
        fields = ["interface_id", "dependent_on_interface"]
        labels = {
            'interface_id': 'Interface ',
        }
