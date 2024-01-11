from django.urls import path
from rest_framework import routers
from .views import RoleCollectionAccessListView, RoleCollectionAccessCreateView, RoleCollectionAccessUpdateView, RoleCollectionAccessDeleteView
from .viewsets import RoleCollectionAccessViewset

router = routers.DefaultRouter()
router.register("rolecollectionaccess", RoleCollectionAccessViewset, basename="rolecollectionaccess")

app_name = "rolecollectionaccess"

urlpatterns = [
    path("list/", RoleCollectionAccessListView.as_view(), name="rolecollectionaccess_list"),
    path("create/", RoleCollectionAccessCreateView.as_view(), name="rolecollectionaccess_create"),
    path("update/<int:pk>/", RoleCollectionAccessUpdateView.as_view(), name="rolecollectionaccess_update", ),
    path("delete/<int:pk>/", RoleCollectionAccessDeleteView.as_view(), name="rolecollectionaccess_delete", ),

]
