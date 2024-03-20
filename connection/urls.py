from django.urls import path
from rest_framework import routers
from .views import (
    ConnectionCreateView,
    ConnectionDeleteView,
    ConnectionListView,
    ConnectionUpdateView,
    HistoricalConnectionListView,
    HistoricalConnectionUpdateView, ConnectionDetailView, ConnectionBulkDeleteView,
)
from .viewsets import ConnectionViewset, ConnectionHistoryViewset, ConnectionDropdownViewset

router = routers.DefaultRouter()
router.register("connection", ConnectionViewset, basename="connection")
router.register(
    "connection/history",
    ConnectionHistoryViewset,
    basename="connection_history",
)
router.register(
    "connection/relations",
    ConnectionDropdownViewset,
    basename="connection_relations",
)

app_name = "connection"

urlpatterns = [
    path("list/", ConnectionListView.as_view(), name="connection_list"),
    path("create/", ConnectionCreateView.as_view(), name="connection_create"),
    path(
        "update/<int:pk>/",
        ConnectionUpdateView.as_view(),
        name="connection_update",
    ),
    path(
        "delete/<int:pk>/",
        ConnectionDeleteView.as_view(),
        name="connection_delete",
    ),
    path(
        "relations/<int:pk>/",
        ConnectionDetailView.as_view(),
        name="connection_relations",
    ),
    path(
        "history/list/<int:pk>/",
        HistoricalConnectionListView.as_view(),
        name="historicalconnection_list",
    ),
    path(
        "history/update/<int:pk>/",
        HistoricalConnectionUpdateView.as_view(),
        name="historicalconnection_update",
    ),
    path("id/<int:pk>/", ConnectionDetailView.as_view(), name="connection_detail"),
    path('bulkDelete/', ConnectionBulkDeleteView.as_view(), name='connection_bulk_delete'),
]
