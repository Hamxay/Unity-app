from django.urls import path
from rest_framework import routers
from .views import (
    FrequencyListView,
    FrequencyCreateView,
    FrequencyUpdateView,
    FrequencyDetailView,
    FrequencyDeleteView,
)
from .viewsets import FrequencyViewset

router = routers.DefaultRouter()
router.register("frequency", FrequencyViewset, basename="frequency")

app_name = "frequency"

urlpatterns = [
    path("frequency/list/", FrequencyListView.as_view(), name="frequency_list"),
    path("frequency/create/", FrequencyCreateView.as_view(), name="frequency_create"),
    path(
        "frequency/update/<int:pk>/",
        FrequencyUpdateView.as_view(),
        name="frequency_update",
    ),
    path(
        "frequency/detail/<int:pk>/",
        FrequencyDetailView.as_view(),
        name="frequency_detail",
    ),
    path(
        "frequency/delete/<int:pk>/",
        FrequencyDeleteView.as_view(),
        name="frequency_delete",
    ),
]
