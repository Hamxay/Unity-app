from django import forms
from .models import Schedule


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = [
            "Name",
            "Frequency",
            "FrequencyInterval",
            "FrequencyRelativeInterval",
            "FrequencyRecurrenceFactor",
            "FrequencySubDayType",
            "FrequencySubDayInterval",
            "ActiveStartDate",
            "ActiveEndDate",
            "ActiveStartTime",
            "ActiveEndTime",
            "IsEnabled",
            "Version",
        ]
        widgets = {
            'ActiveStartDate': forms.DateInput(attrs={'type': 'date'}),
            'ActiveEndDate': forms.DateInput(attrs={'type': 'date'}),
            'ActiveStartTime': forms.TimeInput(attrs={'type': 'time'}),
            'ActiveEndTime': forms.TimeInput(attrs={'type': 'time'}),
        }
        labels = {
            'IsEnabled': ":Is Enabled",
            "FrequencyInterval": "Frequency Interval",
            "FrequencyRelativeInterval": " Frequency Relative Interval",
            "FrequencyRecurrenceFactor": "Frequency Recurrence Factor",
            "FrequencySubDayType": "Frequency Sub DayType",
            "FrequencySubDayInterval": "Frequency Sub Day Interval",
            "ActiveStartDate": "Active Start Date",
            "ActiveEndDate": "Active End Date",
            "ActiveStartTime": "Active Start Time",
            "ActiveEndTime": "Active End Time",
        }
