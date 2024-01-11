from django.urls import path
from rest_framework import routers
from .views import (
    StatusListView,
    StatusCreateView,
    StatusUpdateView,
    StatusDetailView,
    StatusDeleteView,
    StatusGroupListView,
    StatusGroupCreateView,
    StatusGroupUpdateView,
    StatusGroupDetailView,
    StatusGroupDeleteView,
    StatusCriteriaListView,
    StatusCriteriaCreateView,
    StatusCriteriaUpdateView,
    StatusCriteriaDetailView,
    StatusCriteriaDeleteView,
)
from .viewsets import StatusGroupViewset, StatusViewset, StatusCriteriaViewset

router = routers.DefaultRouter()
router.register("status_group", StatusGroupViewset, basename="status_group")
router.register("status", StatusViewset, basename="status")
router.register("status_criteria", StatusCriteriaViewset, basename="status_criteria")

app_name = "status"

urlpatterns = [
    # Status
    path("status/list/", StatusListView.as_view(), name="status_list"),
    path("status/create/", StatusCreateView.as_view(), name="status_create"),
    path("status/update/<int:pk>/", StatusUpdateView.as_view(), name="status_update"),
    path("status/detail/<int:pk>/", StatusDetailView.as_view(), name="status_detail"),
    path("status/delete/<int:pk>/", StatusDeleteView.as_view(), name="status_delete"),
    # StatusGroup
    path("status_group/list/", StatusGroupListView.as_view(), name="status_group_list"),
    path(
        "status_group/create/",
        StatusGroupCreateView.as_view(),
        name="status_group_create",
    ),
    path(
        "status_group/update/<int:pk>/",
        StatusGroupUpdateView.as_view(),
        name="status_group_update",
    ),
    path(
        "status_group/detail/<int:pk>/",
        StatusGroupDetailView.as_view(),
        name="status_group_detail",
    ),
    path(
        "status_group/delete/<int:pk>/",
        StatusGroupDeleteView.as_view(),
        name="status_group_delete",
    ),
    # StatusCriteria
    path(
        "status_criteria/list/",
        StatusCriteriaListView.as_view(),
        name="status_criteria_list",
    ),
    path(
        "status_criteria/create/",
        StatusCriteriaCreateView.as_view(),
        name="status_criteria_create",
    ),
    path(
        "status_criteria/update/<int:pk>/",
        StatusCriteriaUpdateView.as_view(),
        name="status_criteria_update",
    ),
    path(
        "status_criteria/detail/<int:pk>/",
        StatusCriteriaDetailView.as_view(),
        name="status_criteria_detail",
    ),
    path(
        "status_criteria/delete/<int:pk>/",
        StatusCriteriaDeleteView.as_view(),
        name="status_criteria_delete",
    ),
]
