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


class StatusGroup(BaseModel):
    name = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    sort_order = models.IntegerField(blank=False, null=False)

    def __str__(self) -> str:
        return self.name


class Status(BaseModel):
    name = models.CharField(max_length=250, blank=False, null=False)
    display_name = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(max_length=500, blank=False, null=False)
    status_group = models.ForeignKey(StatusGroup, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True, null=True)
    color_hex_code = models.CharField(max_length=50, blank=True, null=True)
    sort_order = models.IntegerField(blank=False, null=False)

    def __str__(self) -> str:
        return self.name


class StatusCriteria(BaseModel):
    kpi = models.ForeignKey(KPI, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    criteria = models.CharField(max_length=255, blank=False, null=False)
