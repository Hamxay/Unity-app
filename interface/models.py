import datetime
from django.db import models
from accounts.models import User
from simple_history.models import HistoricalRecords
from historyconfiguration.models import HistoricalModel
from schedule import models as scheduleModel
from connection import models as connectionModel
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


class InterfaceCategory(BaseModel):
    code = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        db_table = "InterfaceCategory"
        constraints = [
            models.UniqueConstraint(
                fields=["code"], name="UQ__InterfaceCategory__Code"
            ),
        ]

    def __str__(self):
        return f'({self.code} - {self.name})'


class InterfaceType(BaseModel):
    code = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        db_table = "InterfaceType"
        constraints = [
            models.UniqueConstraint(fields=["code"], name="UQ__InterfaceType__Code"),
        ]

    def __str__(self):
        return f'({self.code} - {self.name})'


class Interface(BaseModel):
    WAIT_ACTION_CHOICES = [
        (1, 'Execute Regardless'),
        (2, 'Stop/Do Not Execute'),
    ]
    code = models.BigAutoField(primary_key=True)
    interface_category_id = models.ForeignKey(
        InterfaceCategory, on_delete=models.CASCADE
    )
    interface_type_id = models.ForeignKey(InterfaceType, on_delete=models.CASCADE)
    schedule_id = models.ForeignKey(scheduleModel.Schedule, on_delete=models.CASCADE)
    connection_id = models.ForeignKey(connectionModel.Connection,on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=250, blank=True, null=True)
    priority = models.IntegerField()
    max_concurrent_sessions = models.IntegerField(blank=True, null=True)
    wait_action = models.IntegerField(choices=WAIT_ACTION_CHOICES)
    run_window = models.IntegerField()
    is_enabled = models.BooleanField()  # Assuming 'nchar(1)' stores 'Y' or 'N'
    active_start_date=models.DateField(default=datetime.date.today)
    active_end_date=models.DateField(default=datetime.date.today)
    retry_times = models.IntegerField()

    history = HistoricalRecords(bases=[HistoricalModel])

    class Meta:
        db_table = "Interface"  # Specifies the database table name
        verbose_name = "Interface"
        verbose_name_plural = "Interfaces"

    def save_without_historical_record(self, *args, **kwargs):
        self.skip_history_when_saving = True
        try:
            ret = self.save(*args, **kwargs)
        finally:
            del self.skip_history_when_saving
        return ret

    def __str__(self):
        return f'({self.code} - {self.name})'


class InterfaceDependence(BaseModel):
    code = models.BigAutoField(primary_key=True)
    interface_id = models.ForeignKey(Interface, on_delete=models.CASCADE)
    dependent_on_interface = models.ForeignKey(
        Interface,
        on_delete=models.CASCADE,
        db_column="DependentOnInterfaceId",
        related_name="dependent_interface",
    )

    class Meta:
        db_table = "InterfaceDependence"
        constraints = [
            models.UniqueConstraint(
                fields=["code"], name="UQ__InterfaceDependence__Code"
            ),
        ]
