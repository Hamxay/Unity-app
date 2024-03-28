from django.db import models
from accounts.models import User


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


class Role(BaseModel):
    code = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    ad_group_name = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        db_table = "Role"
        unique_together = [["name", "ad_group_name"]]
        constraints = [
            models.UniqueConstraint(fields=["code"], name="UQ__Role__Code"),
        ]

    def __str__(self):
        return f'({self.code} - {self.name})'