from django.db import models
from accounts.models import User
from simple_history.models import HistoricalRecords


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


class HistoricalModel(models.Model):
    deleted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="%(class)s_deleted_by",
    )
    deleted_date = models.DateTimeField(blank=True, null=True)
    skip_save = models.BooleanField(default=False)

    class Meta:
        abstract = True
        managed = False

    def save(self, *args, **kwargs):
        if not self.skip_save:
            super().save(*args, **kwargs)


class HistoryConfiguration(models.Model):
    model_name = models.CharField(max_length=255, unique=True)
    enable = models.BooleanField(default=False)
    history = HistoricalRecords()
    
    def __str__(self):
        return self.model_name
