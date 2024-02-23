from django import forms
from .models import Collection


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = [
            "interfaceid",
            "name",
            "description",
            "executionorder",
            "executiontriggerrule",
        ]
        labels = {
            'interfaceid': 'Interface ',
            "name": "Name",
            "description": "Description",
            "executionorder": "Execution Order",
            "executiontriggerrule": "Execution Trigger Rule",
        }
