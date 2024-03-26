from django.db import models
from role.models import Role
from collection.models import Collection
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


class RoleCollectionAccess(BaseModel):
    code = models.BigAutoField(primary_key=True)
    collectionId = models.ForeignKey(Collection, on_delete=models.PROTECT, null=False)
    RoleId = models.ForeignKey(Role, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return str(self.code)

    class Meta:
        unique_together = [["collectionId", "RoleId"]]

