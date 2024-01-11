from django.contrib import admin
from .models import KPI, KPISubGroup, KPIGroup


admin.site.register(KPI)
admin.site.register(KPISubGroup)
admin.site.register(KPIGroup)
