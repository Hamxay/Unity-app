from django.urls import path
from rest_framework import routers
from .views import (
    TargetsListView,
    TargetsCreateView,
    TargetsUpdateView,
    TargetsDetailView,
    TargetsDeleteView,
)
from .viewsets import TargetsViewset

router = routers.DefaultRouter()
router.register("targets", TargetsViewset, basename="targets")

app_name = "targets"

urlpatterns = [
    path("targets/list/", TargetsListView.as_view(), name="targets_list"),
    path("targets/create/", TargetsCreateView.as_view(), name="targets_create"),
    path(
        "targets/update/<int:pk>/",
        TargetsUpdateView.as_view(),
        name="targets_update",
    ),
    path(
        "targets/detail/<int:pk>/",
        TargetsDetailView.as_view(),
        name="targets_detail",
    ),
    path(
        "targets/delete/<int:pk>/",
        TargetsDeleteView.as_view(),
        name="targets_delete",
    ),
]
