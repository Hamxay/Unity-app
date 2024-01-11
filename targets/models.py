from django.db import models
from accounts.models import User
from kpi.models import KPI


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


class Targets(BaseModel):
    kpi = models.ForeignKey(KPI, on_delete=models.CASCADE)
    base_line = models.BigIntegerField(blank=True, null=True)
    lower_bound = models.BigIntegerField(blank=False, null=False)
    upper_bound = models.BigIntegerField(blank=False, null=False)
    effective_start_date = models.DateTimeField(blank=False, null=False)
    effective_end_date = models.DateTimeField(blank=False, null=False)
