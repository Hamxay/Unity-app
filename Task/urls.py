
from django.urls import path
from rest_framework import routers
from Task.views import (
    TaskListView,
    HistoricalTaskListView,
    TaskDeleteView,TaskCreateView,TaskUpdateView,HistoricalTaskUpdateView, HistoricalTaskViewAll
)
from Task.viewsets import TaskViewset, TaskHistoryViewset,TaskHistoryViewsetAll

router = routers.DefaultRouter()
router.register("Task", TaskViewset, basename="Task")
# urls.py
router.register(r'Task/history/all', TaskHistoryViewsetAll, basename='Task_history_all')
router.register(r'Task/history', TaskHistoryViewset, basename='Task_history')

app_name = "Task"

urlpatterns = [
    path("list/", TaskListView.as_view(), name="Task_list"),
    path("create/", TaskCreateView.as_view(), name="Task_create"),
    path(
        "update/<int:pk>/",
        TaskUpdateView.as_view(),
        name="Task_update",
    ),
    path(
        "delete/<int:pk>/",
        TaskDeleteView.as_view(),
        name="Task_delete",
    ),
    path(
        "history/list/<int:pk>/",
        HistoricalTaskListView.as_view(),
        name="historicalTask_list",
    ),
    path(
        "history/update/<int:pk>/",
        HistoricalTaskUpdateView.as_view(),
        name="historicalTask_update",
    ),
    path(
        "history_all/",
        HistoricalTaskViewAll.as_view(),
        name="historicalTask_list_all",
    ),
]
