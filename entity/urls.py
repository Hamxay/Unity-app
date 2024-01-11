from django.urls import path
from rest_framework import routers
from .views import (
    EntityListView,
    EntityCreateView,
    EntityUpdateView,
    EntityDetailView,
    EntityDeleteView,
)
from .viewsets import EntityViewset

router = routers.DefaultRouter()
router.register("entity", EntityViewset, basename="Entity")

app_name = "entity"

urlpatterns = [
    path("entity/list/", EntityListView.as_view(), name="entity_list"),
    path("entity/create/", EntityCreateView.as_view(), name="entity_create"),
    path("entity/update/<int:pk>/", EntityUpdateView.as_view(), name="entity_update"),
    path("entity/detail/<int:pk>/", EntityDetailView.as_view(), name="entity_detail"),
    path("entity/delete/<int:pk>/", EntityDeleteView.as_view(), name="entity_delete"),
]
