from django.urls import path
from rest_framework import routers
from .views import StatusUpcomingListView, StatusUpcomingCreateView, StatusUpcomingUpdateView, StatusUpcomingDeleteView, \
    StatusUpcomingBulkDeleteView
from .viewsets import StatusUpcomingViewset

router = routers.DefaultRouter()
router.register("processstatus", StatusUpcomingViewset, basename="processstatus")

app_name = "processstatus"

urlpatterns = [
    path("list/", StatusUpcomingListView.as_view(), name="processstatus_list"),
    path("create/", StatusUpcomingCreateView.as_view(), name="processstatus_create"),
    path("update/<int:pk>/", StatusUpcomingUpdateView.as_view(), name="processstatus_update", ),
    path("delete/<int:pk>/", StatusUpcomingDeleteView.as_view(), name="processstatus_delete", ),
    path('bulkDelete/', StatusUpcomingBulkDeleteView.as_view(),
         name='processstatus_bulk_delete'),
]
