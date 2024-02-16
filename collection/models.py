from django.db import models
from accounts.models import User
from simple_history.models import HistoricalRecords
from historyconfiguration.models import HistoricalModel
from interface.models import Interface


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


class Collection(BaseModel):
    EXECUTION_TRIGGER_RULE = [
        (1, '1 - Success'),
        (2, '2 - Complete'),
    ]
    code = models.BigAutoField(primary_key=True)
    interfaceid = models.ForeignKey(Interface, on_delete=models.PROTECT)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=250, null=True, blank=True)
    executionorder = models.IntegerField()
    executiontriggerrule = models.SmallIntegerField(choices=EXECUTION_TRIGGER_RULE)

    history = HistoricalRecords(bases=[HistoricalModel])

    def save_without_historical_record(self, *args, **kwargs):
        self.skip_history_when_saving = True
        try:
            ret = self.save(*args, **kwargs)
        finally:
            del self.skip_history_when_saving
        return ret

    def __str__(self):
        return f'({self.code} - {self.name})'