from django.urls import path
from rest_framework import routers
from .views import (
    ClassListView,
    HistoricalClassListView,
    ClassDeleteView, ClassCreateView, ClassUpdateView, HistoricalClassUpdateView,
    ClassDropdownView, ClassDetailView, DownloadTemplateView, ImportClassFromFileView
)
from .viewsets import ClassViewset, ClassHistoryViewset, ClassDropdownViewset

router = routers.DefaultRouter()
router.register("class", ClassViewset, basename="class")
router.register(
    "class/history",
    ClassHistoryViewset,
    basename="class_history",
)
router.register("class/relations", ClassDropdownViewset, basename="class_relations")
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
        "id/<int:pk>/",
        ClassDetailView.as_view(),
        name="class_detail",
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
    path(
        "relations/<int:code>",
        ClassDropdownView.as_view(),
        name='class_relations'
    ),
    path('downloadTemplate/', DownloadTemplateView.as_view(), name='downloadTemplate'),
    path('import/', ImportClassFromFileView.as_view(), name='import_class_from_file'),

]
