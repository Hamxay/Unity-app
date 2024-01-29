from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "ClassId",
            "CollectionId",
            "LoadPatternId",
            "Name",
            "Description",
            "ProcessName",
            "ProcessParameters",
            "SubProcessParameters",
            "DeduplicateSource",
            "Priority",
        ]
        labels = {
            'ClassId': 'Class',
            'CollectionId': 'Collection',
            'LoadPatternId': 'LoadPattern',
        }
