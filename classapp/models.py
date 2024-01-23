from django.db import models
from accounts.models import User
from simple_history.models import HistoricalRecords
from collection.models import HistoricalModel



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


class Class(BaseModel):
    Code = models.BigAutoField(primary_key=True)
    InterfaceId = models.IntegerField()
    Name = models.CharField(max_length=128)
    Description = models.CharField(max_length=250, blank=True, null=True)
    Prefix = models.CharField(max_length=50, blank=True, null=True)
    Version = models.IntegerField()
    TargetAlias = models.CharField(max_length=128)
    IgnoreOnIngest = models.CharField(max_length=1)
    Mask = models.TextField(blank=True, null=True)
    Filter = models.TextField(blank=True, null=True)
    SlideWindowAttribute = models.CharField(max_length=128, blank=True, null=True)
    SlideWindowDays = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.Name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["Code"], name="UQ__Class__A25C5AA76C840088")
        ]
        ordering = ["-created_date"]

    history = HistoricalRecords(bases=[HistoricalModel])

    def save_without_historical_record(self, *args, **kwargs):
        self.skip_history_when_saving = True
        try:
            ret = self.save(*args, **kwargs)
        finally:
            del self.skip_history_when_saving
        return ret
