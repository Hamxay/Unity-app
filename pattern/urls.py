from django.urls import path
from rest_framework import routers
from .views import (
    LoadPatternCreateView,
    LoadPatternDeleteView,
    LoadPatternListView,
    LoadPatternUpdateView, LoadPatternDetailView,
)
from .viewsets import LoadPatternViewset

router = routers.DefaultRouter()
router.register("pattern/loadpattern", LoadPatternViewset, basename="loadpattern")

app_name = "pattern"

urlpatterns = [
    path("loadpattern/list/", LoadPatternListView.as_view(), name="load_pattern_list"),
    path(
        "loadpattern/create/",
        LoadPatternCreateView.as_view(),
        name="load_pattern_create",
    ),
    path(
        "loadpattern/update/<int:pk>/",
        LoadPatternUpdateView.as_view(),
        name="load_pattern_update",
    ),
    path(
        "loadpattern/delete/<int:pk>/",
        LoadPatternDeleteView.as_view(),
        name="load_pattern_delete",
    ),
    path(
        "loadpattern/id/<int:pk>/",
        LoadPatternDetailView.as_view(),
        name="pattern_detail",
    ),
]
