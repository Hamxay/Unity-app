from django.urls import path
from rest_framework import routers
from .views import (
    KPIListView,
    KPICreateView,
    KPIUpdateView,
    KPIDetailView,
    KPIDeleteView,
    KPIGroupListView,
    KPIGroupCreateView,
    KPIGroupUpdateView,
    KPIGroupDetailView,
    KPIGroupDeleteView,
    KPISubGroupListView,
    KPISubGroupCreateView,
    KPISubGroupUpdateView,
    KPISubGroupDetailView,
    KPISubGroupDeleteView,
)
from .viewsets import KPIGroupViewset, KPISubGroupViewset, KPIViewset

router = routers.DefaultRouter()
router.register("kpi", KPIViewset, basename="kpi")
router.register("kpi_group", KPIGroupViewset, basename="kpi_group")
router.register("kpi_sub_group", KPISubGroupViewset, basename="kpi_sub_group")

app_name = "kpi"

urlpatterns = [
    # KPI
    path("kpi/list/", KPIListView.as_view(), name="kpi_list"),
    path("kpi/create/", KPICreateView.as_view(), name="kpi_create"),
    path("kpi/update/<int:pk>/", KPIUpdateView.as_view(), name="kpi_update"),
    path("kpi/detail/<int:pk>/", KPIDetailView.as_view(), name="kpi_detail"),
    path("kpi/delete/<int:pk>/", KPIDeleteView.as_view(), name="kpi_delete"),
    # KPIGroup
    path("kpi_group/list/", KPIGroupListView.as_view(), name="kpi_group_list"),
    path("kpi_group/create/", KPIGroupCreateView.as_view(), name="kpi_group_create"),
    path(
        "kpi_group/update/<int:pk>/",
        KPIGroupUpdateView.as_view(),
        name="kpi_group_update",
    ),
    path(
        "kpi_group/detail/<int:pk>/",
        KPIGroupDetailView.as_view(),
        name="kpi_group_detail",
    ),
    path(
        "kpi_group/delete/<int:pk>/",
        KPIGroupDeleteView.as_view(),
        name="kpi_group_delete",
    ),
    # KPISubGroup
    path(
        "kpi_sub_group/list/", KPISubGroupListView.as_view(), name="kpi_sub_group_list"
    ),
    path(
        "kpi_sub_group/create/",
        KPISubGroupCreateView.as_view(),
        name="kpi_sub_group_create",
    ),
    path(
        "kpi_sub_group/update/<int:pk>/",
        KPISubGroupUpdateView.as_view(),
        name="kpi_sub_group_update",
    ),
    path(
        "kpi_sub_group/detail/<int:pk>/",
        KPISubGroupDetailView.as_view(),
        name="kpi_sub_group_detail",
    ),
    path(
        "kpi_sub_group/delete/<int:pk>/",
        KPISubGroupDeleteView.as_view(),
        name="kpi_sub_group_delete",
    ),
]
