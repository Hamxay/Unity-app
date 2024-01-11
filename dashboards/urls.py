from django.urls import path
from dashboards.views import (
    dashboard_view,
    ProfileUpdateView,
    NotificationListView,
    NotificationDeleteView,
)
from report.views import ReportListView

app_name = "dashboards"

urlpatterns = [
    path("profile/<int:pk>/", ProfileUpdateView.as_view(), name="user_profile"),
    # path("", view=dashboard_view, name="dashboard"),
    path("", ReportListView.as_view(), name="dashboard"),
    path(
        "notification-list/", NotificationListView.as_view(), name="notification_list"
    ),
    path(
        "notification-delete/<int:pk>/",
        NotificationDeleteView.as_view(),
        name="notification_delete",
    ),
]
