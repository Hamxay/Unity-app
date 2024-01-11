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
    Code = models.IntegerField(unique=True)
    Name = models.CharField(max_length=128)
    Frequency = models.IntegerField()
    FrequencyInterval = models.IntegerField()
    FrequencyRelativeInterval = models.IntegerField()
    FrequencyRecurrenceFactor = models.IntegerField()
    FrequencySubDayType = models.IntegerField()
    FrequencySubDayInterval = models.IntegerField()
    ActiveStartDate = models.IntegerField()
    ActiveEndDate = models.IntegerField()
    ActiveStartTime = models.IntegerField()
    ActiveEndTime = models.IntegerField()
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
        return f"{self.Code} - {self.Name}"
