from django.contrib import admin
from .models import StatusGroup, Status, StatusCriteria

admin.site.register(StatusGroup)
admin.site.register(Status)
admin.site.register(StatusCriteria)
