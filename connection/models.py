from django.db import models
from accounts.models import User
from simple_history.models import HistoricalRecords
from historyconfiguration.models import HistoricalModel


# Create your models here.
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


class Connection(BaseModel):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=250, blank=True, null=True)
    connection_string = models.TextField(blank=True, null=True)

    history = HistoricalRecords(bases=[HistoricalModel])

    def save_without_historical_record(self, *args, **kwargs):
        self.skip_history_when_saving = True
        try:
            ret = self.save(*args, **kwargs)
        finally:
            del self.skip_history_when_saving
        return ret
