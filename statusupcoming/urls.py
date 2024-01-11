from django.urls import path
from rest_framework import routers
from .views import StatusUpcomingListView, StatusUpcomingCreateView, StatusUpcomingUpdateView, StatusUpcomingDeleteView
from .viewsets import StatusUpcomingViewset

router = routers.DefaultRouter()
router.register("statusupcoming", StatusUpcomingViewset, basename="statusupcoming")

app_name = "statusupcoming"

urlpatterns = [
    path("list/", StatusUpcomingListView.as_view(), name="statusupcoming_list"),
    path("create/", StatusUpcomingCreateView.as_view(), name="statusupcoming_create"),
    path("update/<int:pk>/", StatusUpcomingUpdateView.as_view(), name="statusupcoming_update", ),
    path("delete/<int:pk>/", StatusUpcomingDeleteView.as_view(), name="statusupcoming_delete", ),

]
