from django.urls import path
from .views import ConfigListView


app_name = "historyconfiguration"

urlpatterns = [
    path("list/", ConfigListView.as_view(), name="historyconfiguration_list"),
]
