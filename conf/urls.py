"""
URL configuration for conf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from entity.urls import router as entity_routers
from report.urls import router as report_routers
from kpi.urls import router as kpi_routers
from frequency.urls import router as frequency_routers
from status.urls import router as status_routers
from trend.urls import router as trend_routers
from targets.urls import router as targets_routers
from attribute.urls import router as attribute_routers
from logs.urls import router as logs_routers
from classapp.urls import router as class_router
from collection.urls import router as collection_router
from connection.urls import router as connection_router
from interface.urls import router as Interface_router
from pattern.urls import router as pattern_router
from role.urls import router as role_router
from Task.urls import router as Task_router
from rolecollectionaccess.urls import router as rolecollectionaccess_router
from processstatus.urls import router as processstatus_router
from schedule.urls import router as schedule_router


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

# Extend Leads app DRF Routers
router.registry.extend(entity_routers.registry)
router.registry.extend(report_routers.registry)
router.registry.extend(kpi_routers.registry)
router.registry.extend(frequency_routers.registry)
router.registry.extend(status_routers.registry)
router.registry.extend(trend_routers.registry)
router.registry.extend(targets_routers.registry)
router.registry.extend(attribute_routers.registry)
router.registry.extend(logs_routers.registry)
router.registry.extend(class_router.registry)
router.registry.extend(collection_router.registry)
router.registry.extend(connection_router.registry)
router.registry.extend(Interface_router.registry)
router.registry.extend(pattern_router.registry)
router.registry.extend(role_router.registry)
router.registry.extend(Task_router.registry)
router.registry.extend(rolecollectionaccess_router.registry)
router.registry.extend(processstatus_router.registry)
router.registry.extend(schedule_router.registry)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("dashboards.urls")),
    path("report/", include("report.urls")),
    path("accounts/", include("allauth.urls")),
    path("entity/", include("entity.urls")),
    path("kpi/", include("kpi.urls")),
    path("frequency/", include("frequency.urls")),
    path("status/", include("status.urls")),
    path("trend/", include("trend.urls")),
    path("targets/", include("targets.urls")),
    path("attribute/", include("attribute.urls")),
    path("logs/", include("logs.urls")),
    path("pattern/", include("pattern.urls")),
    path("role/", include("role.urls")),
    path("class/", include("classapp.urls")),
    path("collection/", include("collection.urls")),
    path("connection/", include("connection.urls")),
    path("interface/", include("interface.urls")),
    path("historyconfiguration/", include("historyconfiguration.urls")),
    path("api/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    path("Task/", include("Task.urls")),
    path("rolecollectionaccess/", include("rolecollectionaccess.urls")),
    path("processstatus/", include("processstatus.urls")),
    path("schedule/",include("schedule.urls")),
]
