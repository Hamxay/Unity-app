from django import forms
from .models import Collection


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = [
            "precedingcollectionid",
            "interfaceid",
            "name",
            "description",
            "executionorder",
            "executiontriggerrule",
        ]
        labels = {
            'interfaceid': 'Interface ',
        }

