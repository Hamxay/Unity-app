import datetime
from django.utils import timezone

from django.db import models
from accounts.models import User
from simple_history.models import HistoricalRecords
from historyconfiguration.models import HistoricalModel


class BaseModel(models.Model):
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="%(class)s_created_by"
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="%(class)s_updated_by",
    )
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_date"]


class Schedule(BaseModel):
    FREQUENCY_CHOICES = [
        (0, '0 - Once'),
        (1, '1 - Daily'),
        (2, '2 - Weekly'),
        (3, '3 - Monthly'),
        (4, '4 - Monthly-Relative'),
    ]

    FREQUENCY_SUB_DAY_TYPE_CHOICES = [
        (1, '1 - Minutes'),
        (2, '2 - Hourly'),
    ]

    FREQUENCY_RELATIVE_INTERVAL_CHOICES = [
        (0, '0 - Unused'),
        (1, '1 - First'),
        (2, '2 - Second'),
        (3, '3 - Third'),
        (4, '4 - Fourth'),
        (5, '5 - Last'),
    ]
    Code = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=128, unique=True)
    Frequency = models.IntegerField(choices=FREQUENCY_CHOICES)
    FrequencyInterval = models.IntegerField()
    FrequencyRelativeInterval = models.IntegerField(choices=FREQUENCY_RELATIVE_INTERVAL_CHOICES)
    FrequencyRecurrenceFactor = models.IntegerField()
    FrequencySubDayType = models.IntegerField(choices=FREQUENCY_SUB_DAY_TYPE_CHOICES)
    FrequencySubDayInterval = models.IntegerField()
    ActiveStartDate = models.DateField(default=datetime.date.today)
    ActiveEndDate = models.DateField(default=datetime.date.today)
    ActiveStartTime = models.TimeField()
    ActiveEndTime = models.TimeField()
    IsEnabled = models.BooleanField(max_length=1)
    Version = models.IntegerField()

    history = HistoricalRecords(bases=[HistoricalModel])

    def save_without_historical_record(self, *args, **kwargs):
        self.skip_history_when_saving = True
        try:
            ret = self.save(*args, **kwargs)
        finally:
            del self.skip_history_when_saving
        return ret

    def __str__(self):
        return f"({self.Code} - {self.Name})"
