from django.urls import path
from rest_framework import routers
from .views import (
    ReportListView,
    ReportCreateView,
    ReportUpdateView,
    ReportDetailView,
    ReportDeleteView,
)
from .viewsets import ReportViewset

router = routers.DefaultRouter()
router.register("report", ReportViewset, basename="report")

app_name = "report"

urlpatterns = [
    path("report/list/", ReportListView.as_view(), name="report_list"),
    path("report/create/", ReportCreateView.as_view(), name="report_create"),
    path("report/update/<int:pk>/", ReportUpdateView.as_view(), name="report_update"),
    path("report/detail/<int:pk>/", ReportDetailView.as_view(), name="report_detail"),
    path("report/delete/<int:pk>/", ReportDeleteView.as_view(), name="report_delete"),
]
