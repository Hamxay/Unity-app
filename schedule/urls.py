from django.urls import path
from rest_framework import routers
from .views import (
    ScheduleListView,
    ScheduleCreateView,
    ScheduleDeleteView,
    ScheduleUpdateView,
    HistoricalScheduleListView,
    HistoricalScheduleUpdateView
)
from .viewsets import ScheduleViewset, ScheduleHistoryViewset

router = routers.DefaultRouter()
router.register("schedule", ScheduleViewset, basename="schedule")
router.register(
    "schedule/history",
    ScheduleHistoryViewset,
    basename="schedule_history",
)

app_name = "schedule"

urlpatterns = [
    path("list/", ScheduleListView.as_view(), name="schedule_list"),
    path("create/", ScheduleCreateView.as_view(), name="schedule_create"),
    path(
        "update/<slug:Code>/",
        ScheduleUpdateView.as_view(),
        name="schedule_update",
    ),
    path(
        "delete/<slug:Code>/",
        ScheduleDeleteView.as_view(),
        name="schedule_delete",
    ),
    path(
        "history/list/<int:pk>/",
        HistoricalScheduleListView.as_view(),
        name="historicalschedule_list",
    ),
    path(
        "history/update/<int:pk>/",
        HistoricalScheduleUpdateView.as_view(),
        name="historicalschedule_update",
    ),
]
