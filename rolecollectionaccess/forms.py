from django import forms
from .models import RoleCollectionAccess


class RoleCollectionAccessForm(forms.ModelForm):
    class Meta:
        model = RoleCollectionAccess
        fields = ["collectionId", "RoleId"]
        labels = {
            'collectionId': 'collection',
            'RoleId': 'Role',
        }
