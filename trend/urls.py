from django.urls import path
from rest_framework import routers
from .views import (
    TrendListView,
    TrendCreateView,
    TrendUpdateView,
    TrendDetailView,
    TrendDeleteView,
    TrendCriteriaListView,
    TrendCriteriaCreateView,
    TrendCriteriaUpdateView,
    TrendCriteriaDetailView,
    TrendCriteriaDeleteView,
)
from .viewsets import TrendViewset, TrendCriteriaViewset

router = routers.DefaultRouter()
router.register("trend", TrendViewset, basename="trend")
router.register("trend_criteria", TrendCriteriaViewset, basename="trend_criteria")

app_name = "trend"

urlpatterns = [
    # Trend
    path("trend/list/", TrendListView.as_view(), name="trend_list"),
    path("trend/create/", TrendCreateView.as_view(), name="trend_create"),
    path("trend/update/<int:pk>/", TrendUpdateView.as_view(), name="trend_update"),
    path("trend/detail/<int:pk>/", TrendDetailView.as_view(), name="trend_detail"),
    path("trend/delete/<int:pk>/", TrendDeleteView.as_view(), name="trend_delete"),
    # TrendCriteria
    path(
        "trend_criteria/list/",
        TrendCriteriaListView.as_view(),
        name="trend_criteria_list",
    ),
    path(
        "trend_criteria/create/",
        TrendCriteriaCreateView.as_view(),
        name="trend_criteria_create",
    ),
    path(
        "trend_criteria/update/<int:pk>/",
        TrendCriteriaUpdateView.as_view(),
        name="trend_criteria_update",
    ),
    path(
        "trend_criteria/detail/<int:pk>/",
        TrendCriteriaDetailView.as_view(),
        name="trend_criteria_detail",
    ),
    path(
        "trend_criteria/delete/<int:pk>/",
        TrendCriteriaDeleteView.as_view(),
        name="trend_criteria_delete",
    ),
]
