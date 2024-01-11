from django.urls import path
from rest_framework import routers
from .views import (
    APIIngestionBatchStatusLogDetailView,
    APIIngestionBatchStatusLogListView,
    CheckpointLogListView,
    AuditLogListView,
    RunLogListView,
    RunStepLogListView
)
from .viewsets import (
    APIIngestionBatchStatusLogListViewset,
    CheckpointLogListViewset,
    AuditLogListViewset,
    RunLogListViewset,
    RunStepLogListViewset
)

router = routers.DefaultRouter()
router.register(
    "APIIngestionBatchStatusLog",
    APIIngestionBatchStatusLogListViewset,
    basename="APIIngestionBatchStatusLog",
)

router.register(
    "CheckpointLog",
    CheckpointLogListViewset,
    basename="CheckpointLog",
)
router.register(
    "AuditLog",
    AuditLogListViewset,
    basename="AuditLog",
)
router.register(
    "RunLog",
    RunLogListViewset,
    basename="RunLog",
)
router.register(
    "RunStepLog",
    RunStepLogListViewset,
    basename="RunStepLog",
)

app_name = "logs"

urlpatterns = [
    path(
        "APIIngestionBatchStatusLog/list/",
        APIIngestionBatchStatusLogListView.as_view(),
        name="APIIngestionBatchStatusLog_list",
    ),
    path(
        "CheckpointLog/list/",
        CheckpointLogListView.as_view(),
        name="CheckpointLogLog_list",
    ),
    path(
        "AuditLog/list/",
        AuditLogListView.as_view(),
        name="AuditLog_list",
    ),
    path(
        "RunLog/list/",
        RunLogListView.as_view(),
        name="RunLog_list",
    ),
    path(
        "RunStepLog/list/",
        RunStepLogListView.as_view(),
        name="RunStepLog_list",
    ),
    path(
        "APIIngestionBatchStatusLog/detail/<int:pk>/",
        APIIngestionBatchStatusLogDetailView.as_view(),
        name="APIIngestionBatchStatusLog_detail",
    ),
]
