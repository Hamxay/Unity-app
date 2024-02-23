from django import forms
from .models import Attribute


class AttributeForm(forms.ModelForm):
    class Meta:
        model = Attribute
        fields = [
            "class_id",
            "source_name",
            "target_name",
            "source_description",
            "target_description",
            "source_ordinal_position",
            "target_ordinal_position",
            "source_data_type",
            "target_data_type",
            "source_max_length",
            "target_max_length",
            "source_precision",
            "target_precision",
            "source_scale",
            "target_scale",
            "is_primary_key",
            "is_snapshot_key",
            "is_nullable",
            "ignore_on_ingest",
        ]
        labels = {
            'class_id': 'Class',
        }


class ImportFileForm(forms.Form):
    file = forms.FileField()
