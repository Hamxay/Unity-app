from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User
from classapp.models import Class
from collection.models import Collection
from pattern.models import LoadPattern
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


class Task(BaseModel):
    Code = models.BigAutoField(primary_key=True)
    ClassId = models.ForeignKey(Class, on_delete=models.CASCADE)
    CollectionId = models.ForeignKey(Collection, on_delete=models.CASCADE)
    LoadPatternId = models.ForeignKey(LoadPattern, on_delete=models.CASCADE)
    Name = models.CharField(max_length=128)
    Description = models.CharField(max_length=250, null=True)
    ProcessName = models.CharField(max_length=128)
    ProcessParameters = models.CharField(max_length=2000, null=True)
    SubProcessParameters = models.CharField(max_length=2000, null=True)
    DeduplicateSource = models.BooleanField(default=False)
    Priority = models.IntegerField(null=True)

    def __str__(self):
        return self.Name

    class Meta:
        db_table = 'Task'

    # Create your models here.
    history = HistoricalRecords(bases=[HistoricalModel])

    def save_without_historical_record(self, *args, **kwargs):
        self.skip_history_when_saving = True
        try:
            ret = self.save(*args, **kwargs)
        finally:
            del self.skip_history_when_saving
        return ret
