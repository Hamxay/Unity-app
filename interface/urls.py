from django.urls import path,include
from rest_framework import routers
from .views import (
    HistoricalInterfaceListView,
    HistoricalInterfaceUpdateView,
    InterfaceCategoryCreateView,
    InterfaceCategoryDeleteView,
    InterfaceCategoryListView,
    InterfaceCategoryUpdateView,
    InterfaceCreateView,
    InterfaceDeleteView,
    InterfaceDependenceCreateView,
    InterfaceDependenceDeleteView,
    InterfaceDependenceListView,
    InterfaceDependenceUpdateView,
    InterfaceListView,
    InterfaceTypeCreateView,
    InterfaceTypeDeleteView,
    InterfaceTypeListView,
    InterfaceTypeUpdateView,
    InterfaceUpdateView, InterfaceDropdownView, InterfaceTypeDetailView, InterfaceCategoryDetailView,
    InterfaceDetailView, InterfaceBulkDeleteView, InterfaceCategoryBulkDeleteView, InterfaceDependenceBulkDeleteView,
    InterfaceTypeBulkDeleteView,
)
from .viewsets import (
    InterfaceCategoryViewset,
    InterfaceDependenceViewset,
    InterfaceHistoryViewset,
    InterfaceTypeViewset,
    InterfaceViewset,
    InterfaceDropdownViewSet, InterfaceTypeDetailViewSet
)

router = routers.DefaultRouter()
router.register(
    "interface/category", InterfaceCategoryViewset, basename="interface_category"
)
router.register("interface/type", InterfaceTypeViewset, basename="interface_type")
router.register(
    "interface/dependence", InterfaceDependenceViewset, basename="interface_dependence"
)
router.register("interface", InterfaceViewset, basename="interface")
router.register("references", InterfaceDropdownViewSet, basename="references")
router.register("interface/type/relations", InterfaceTypeDetailViewSet, basename="interface_type_relations")
router.register(
    "interface/history",
    InterfaceHistoryViewset,
    basename="history",
)

app_name = "interface"

urlpatterns = [
    path(
        "category/list/",
        InterfaceCategoryListView.as_view(),
        name="interface_category_list",
    ),
    path(
        "category/create/",
        InterfaceCategoryCreateView.as_view(),
        name="interface_category_create",
    ),
    path(
        "category/update/<int:pk>/",
        InterfaceCategoryUpdateView.as_view(),
        name="interface_category_update",
    ),
    path(
        "category/delete/<int:pk>/",
        InterfaceCategoryDeleteView.as_view(),
        name="interface_category_delete",
    ),
    path(
        "type/list/",
        InterfaceTypeListView.as_view(),
        name="interface_type_list",
    ),
    path(
        "type/relations/",
        InterfaceTypeDetailView.as_view(),
        name="interface_type_relations",
    ),
    path(
        "type/create/",
        InterfaceTypeCreateView.as_view(),
        name="interface_type_create",
    ),
    path(
        "type/update/<int:pk>/",
        InterfaceTypeUpdateView.as_view(),
        name="interface_type_update",
    ),
    path(
        "type/delete/<int:pk>/",
        InterfaceTypeDeleteView.as_view(),
        name="interface_type_delete",
    ),
    path("list/", InterfaceListView.as_view(), name="interface_list"),
    path("create/", InterfaceCreateView.as_view(), name="interface_create"),
    path(
        "update/<int:pk>/",
        InterfaceUpdateView.as_view(),
        name="interface_update",
    ),
    path(
        "delete/<int:pk>/",
        InterfaceDeleteView.as_view(),
        name="interface_delete",
    ),
    path(
        "history/list/<int:pk>/",
        HistoricalInterfaceListView.as_view(),
        name="historicalinterface_list",
    ),
    path(
        "history/update/<int:pk>/",
        HistoricalInterfaceUpdateView.as_view(),
        name="historicalinterface_update",
    ),
    path(
        "dependence/list/",
        InterfaceDependenceListView.as_view(),
        name="interface_dependence_list",
    ),
    path(
        "dependence/create/",
        InterfaceDependenceCreateView.as_view(),
        name="interface_dependence_create",
    ),
    path(
        "dependence/update/<int:pk>/",
        InterfaceDependenceUpdateView.as_view(),
        name="interface_dependence_update",
    ),
    path(
        "dependence/delete/<int:pk>/",
        InterfaceDependenceDeleteView.as_view(),
        name="interface_dependence_delete",
    ),
    path(
        "references/<int:pk>",
        InterfaceDropdownView.as_view(),
        name='references'
    ),
    path("type/id/<int:pk>/", InterfaceTypeDetailView.as_view(), name="interface_type_detail"),
    path("category/id/<int:pk>/", InterfaceCategoryDetailView.as_view(), name="interface_category_detail"),
    path("id/<int:pk>/", InterfaceDetailView.as_view(), name="interface_detail"),
    path('bulkDelete/', InterfaceBulkDeleteView.as_view(), name='interface_bulk_delete'),
    path('category/bulkDelete/', InterfaceCategoryBulkDeleteView.as_view(), name='interface_category_bulk_delete'),
    path('type/bulkDelete/', InterfaceTypeBulkDeleteView.as_view(), name='interface_type_bulk_delete'),
    path('dependence/bulkDelete/', InterfaceDependenceBulkDeleteView.as_view(), name='interface_dependence_bulk_delete'),

]
