from django.urls import path
from rest_framework import routers
from .views import (
    CollectionListView,
    HistoricalCollectionListView,
    CollectionDeleteView, CollectionCreateView, CollectionUpdateView, HistoricalCollectionUpdateView,
    CollectionDetailView, CollectionBulkDeleteView
)
from .viewsets import CollectionViewset, CollectionHistoryViewset, CollectionRelationsViewset

router = routers.DefaultRouter()
router.register("collection", CollectionViewset, basename="collection")
router.register("collection/relations", CollectionRelationsViewset, basename="collection_relations")
router.register(
    "collection/history",
    CollectionHistoryViewset,
    basename="collection_history",
)

app_name = "collection"

urlpatterns = [
    path("list/", CollectionListView.as_view(), name="collection_list"),
    path("create/", CollectionCreateView.as_view(), name="collection_create"),
    path(
        "update/<int:pk>/",
        CollectionUpdateView.as_view(),
        name="collection_update",
    ),
    path(
        "delete/<int:pk>/",
        CollectionDeleteView.as_view(),
        name="collection_delete",
    ),
    path(
        "history/list/<int:pk>/",
        HistoricalCollectionListView.as_view(),
        name="historicalcollection_list",
    ),
    path(
        "history/update/<int:pk>/",
        HistoricalCollectionUpdateView.as_view(),
        name="historicalcollection_update",
    ),
    path(
        "relations/<int:pk>/",
        CollectionDetailView.as_view(),
        name='collection_relations'
    ),
    path('bulkDelete/', CollectionBulkDeleteView.as_view(), name='collection_bulk_delete'),

]
