from django.db import models
from accounts.models import User
from entity.models import Entity
from frequency.models import Frequency


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


class KPIGroup(BaseModel):
    name = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    sort_order = models.IntegerField(blank=False, null=False)

    def __str__(self) -> str:
        return self.name


class KPISubGroup(BaseModel):
    name = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    group = models.ForeignKey(KPIGroup, on_delete=models.CASCADE)
    sort_order = models.IntegerField(blank=False, null=False)

    def __str__(self) -> str:
        return self.name


class KPI(BaseModel):
    TYPE_CHOICES = [
        ("Benchmark", "Benchmark"),
        ("Target", "Target"),
    ]
    VALUE_TYPE_CHOICES = [
        ("Number", "Number"),
        ("Percentage", "Percentage"),
        ("Text", "Text"),
    ]
    PRIOR_PERIOD_CHANGE_POSITIVE_CHOICES = [
        ("Y", "Y"),
        ("N", "N"),
    ]

    name = models.CharField(max_length=250, blank=False, null=False)
    display_name = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        default="Benchmark",
    )
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    kpi_sub_group = models.ForeignKey(KPISubGroup, on_delete=models.CASCADE)
    frequency = models.ForeignKey(Frequency, on_delete=models.CASCADE)
    value_type = models.CharField(
        max_length=50,
        choices=VALUE_TYPE_CHOICES,
        default="Number",
    )
    value_format = models.CharField(max_length=50, blank=False, null=False)
    query_definition = models.CharField(max_length=255, blank=False, null=False)
    no_of_periods_to_show = models.IntegerField(blank=True, null=True)
    prior_period_change_is_positive = models.CharField(
        max_length=1,
        choices=PRIOR_PERIOD_CHANGE_POSITIVE_CHOICES,
        default="Y",
    )
    key_measure_priority_order = models.IntegerField(blank=False, null=False)
    sort_order = models.IntegerField(blank=False, null=False)
    related_report_link = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
