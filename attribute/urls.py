from django.urls import path
from rest_framework import routers
from .views import (
    AttributeListView,
    AttributeCreateView,
    AttributeUpdateView,
    AttributeDeleteView,
    HistoricalAttributeListView,
    HistoricalAttributeUpdateView, AttributeDownloadTemplateView, AttributeImportClassFromFileView,
    AttributeBulkDeleteView,
)
from .viewsets import AttributeViewset, AttributeHistoryViewset

router = routers.DefaultRouter()
router.register("attribute", AttributeViewset, basename="attribute")
router.register(
    "attribute/history",
    AttributeHistoryViewset,
    basename="attribute_history",
)

app_name = "attribute"

urlpatterns = [
    path("list/", AttributeListView.as_view(), name="attribute_list"),
    path("create/", AttributeCreateView.as_view(), name="attribute_create"),
    path(
        "update/<int:pk>/",
        AttributeUpdateView.as_view(),
        name="attribute_update",
    ),
    path(
        "delete/<int:pk>/",
        AttributeDeleteView.as_view(),
        name="attribute_delete",
    ),
    path(
        "history/list/<int:pk>/",
        HistoricalAttributeListView.as_view(),
        name="historicalattribute_list",
    ),
    path(
        "history/update/<int:pk>/",
        HistoricalAttributeUpdateView.as_view(),
        name="historicalattribute_update",
    ),
    path('downloadTemplate/', AttributeDownloadTemplateView.as_view(), name='downloadTemplate'),
    path('import/', AttributeImportClassFromFileView.as_view(), name='import_class_from_file'),
    path('bulkDelete/', AttributeBulkDeleteView.as_view(), name='attribute_bulk_delete'),
]
