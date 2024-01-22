from django.urls import path
from rest_framework import routers
from .views import (
    ConnectionCreateView,
    ConnectionDeleteView,
    ConnectionListView,
    ConnectionUpdateView,
    HistoricalConnectionListView,
    HistoricalConnectionUpdateView,
)
from .viewsets import ConnectionViewset, ConnectionHistoryViewset

router = routers.DefaultRouter()
router.register("connection", ConnectionViewset, basename="connection")
router.register(
    "connection/history",
    ConnectionHistoryViewset,
    basename="connection_history",
)

app_name = "connection"

urlpatterns = [
    path("list/", ConnectionListView.as_view(), name="connection_list"),
    path("create/", ConnectionCreateView.as_view(), name="connection_create"),
    path(
        "update/<slug:code>/",
        ConnectionUpdateView.as_view(),
        name="connection_update",
    ),
    path(
        "delete/<slug:code>/",
        ConnectionDeleteView.as_view(),
        name="connection_delete",
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
]
