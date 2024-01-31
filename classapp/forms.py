from django import forms
from .models import Class


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = [
            "InterfaceId",
            "Name",
            "Description",
            "Prefix",
            "Version",
            "TargetAlias",
            "IgnoreOnIngest",
            "Mask",
            "Filter",
            "SlideWindowAttribute",
            "SlideWindowDays",
        ]
        labels = {
            'InterfaceId': 'Interface',
        }


class ImportFileForm(forms.Form):
    file = forms.FileField()
