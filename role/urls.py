from django.urls import path
from rest_framework import routers
from .views import RoleListView, RoleCreateView, RoleUpdateView, RoleDeleteView
from .viewsets import RoleViewset

router = routers.DefaultRouter()
router.register("role", RoleViewset, basename="role")

app_name = "role"

urlpatterns = [
    path("list/", RoleListView.as_view(), name="role_list"),
    path("create/", RoleCreateView.as_view(), name="role_create"),
    path(
        "update/<int:pk>/",
        RoleUpdateView.as_view(),
        name="role_update",
    ),
    path(
        "delete/<int:pk>/",
        RoleDeleteView.as_view(),
        name="role_delete",
    ),
]
