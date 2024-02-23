from django.urls import path
from rest_framework import routers
from .views import (
    ScheduleListView,
    ScheduleCreateView,
    ScheduleDeleteView,
    ScheduleUpdateView,
    HistoricalScheduleListView,
    HistoricalScheduleUpdateView, ScheduleDetailView
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
        "update/<int:pk>/",
        ScheduleUpdateView.as_view(),
        name="schedule_update",
    ),
    path(
        "delete/<int:pk>/",
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
    path("id/<int:pk>/", ScheduleDetailView.as_view(), name="schedule_detail"),

]
