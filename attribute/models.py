from django.db import models
from accounts.models import User
from simple_history.models import HistoricalRecords

from classapp.models import Class
from collection.models import HistoricalModel


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


class Attribute(BaseModel):
    code = models.BigAutoField(primary_key=True)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    source_name = models.CharField(max_length=128)
    target_name = models.CharField(max_length=128)
    source_description = models.CharField(max_length=250, null=True)
    target_description = models.CharField(max_length=250, null=True)
    source_ordinal_position = models.IntegerField()
    target_ordinal_position = models.IntegerField()
    source_data_type = models.CharField(max_length=128)
    target_data_type = models.CharField(max_length=128)
    source_max_length = models.IntegerField(null=True)
    target_max_length = models.IntegerField(null=True)
    source_precision = models.IntegerField(null=True)
    target_precision = models.IntegerField(null=True)
    source_scale = models.IntegerField(null=True)
    target_scale = models.IntegerField(null=True)
    is_primary_key = models.CharField(max_length=1)
    is_snapshot_key = models.CharField(max_length=1)
    is_nullable = models.CharField(max_length=1)
    ignore_on_ingest = models.CharField(max_length=1)

    history = HistoricalRecords(bases=[HistoricalModel])

    def save_without_historical_record(self, *args, **kwargs):
        self.skip_history_when_saving = True
        try:
            ret = self.save(*args, **kwargs)
        finally:
            del self.skip_history_when_saving
        return ret
