from django import forms
from django.forms import modelformset_factory
from .models import HistoryConfiguration

ConfigurationFormSet = modelformset_factory(HistoryConfiguration, fields=('enable',), extra=0)

