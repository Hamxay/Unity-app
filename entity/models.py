from django.db import models
from accounts.models import User
from report.models import Report


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


class Entity(BaseModel):
    name = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(max_length=500, blank=False, null=False)
    entity_table_name = models.CharField(max_length=250, blank=False, null=False)
    entity_key_column = models.CharField(max_length=250, blank=False, null=False)
    entity_name_column = models.CharField(max_length=250, blank=False, null=False)
    entity_other_attributes = models.CharField(max_length=1000, blank=True, null=True)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
