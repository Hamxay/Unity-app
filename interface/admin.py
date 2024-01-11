from django.contrib import admin
from .models import Interface, InterfaceCategory, InterfaceType, InterfaceDependence

admin.site.register(Interface)
admin.site.register(InterfaceCategory)
admin.site.register(InterfaceType)
admin.site.register(InterfaceDependence)
