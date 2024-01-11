from django.urls import path
from rest_framework import routers
from .views import (
    ClassListView,
    HistoricalClassListView,
    ClassDeleteView,ClassCreateView,ClassUpdateView,HistoricalClassUpdateView
)
from .viewsets import ClassViewset, ClassHistoryViewset

router = routers.DefaultRouter()
router.register("class", ClassViewset, basename="class")
router.register(
    "class/history",
    ClassHistoryViewset,
    basename="class_history",
)

app_name = "class"

urlpatterns = [
    path("list/", ClassListView.as_view(), name="class_list"),
    path("create/", ClassCreateView.as_view(), name="class_create"),
    path(
        "update/<int:pk>/",
        ClassUpdateView.as_view(),
        name="class_update",
    ),
    path(
        "delete/<int:pk>/",
        ClassDeleteView.as_view(),
        name="class_delete",
    ),
    path(
        "history/list/<int:pk>/",
        HistoricalClassListView.as_view(),
        name="historicalclass_list",
    ),
    path(
        "history/update/<int:pk>/",
        HistoricalClassUpdateView.as_view(),
        name="historicalclass_update",
    ),
]
