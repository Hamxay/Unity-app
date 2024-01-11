from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class Notification(BaseModel):
    class Type(models.IntegerChoices):
        ERROR = 1
        WARNING = 2
        TIP = 3

    subject = models.TextField(blank=True)
    message = models.TextField(blank=True)
    type = models.IntegerField(choices=Type.choices)

    class Meta:
        ordering = ["-created"]



