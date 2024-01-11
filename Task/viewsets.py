from rest_framework.response import Response
from rest_framework import viewsets
from Task.models import Task
from Task.serializer import TaskHistorySerializer, TaskSerializer


class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskHistoryViewsetAll(viewsets.ReadOnlyModelViewSet):
    queryset = Task.history.all()
    serializer_class = TaskHistorySerializer


class TaskHistoryViewset(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Task.history.filter(id=pk)
        serializer = TaskHistorySerializer(queryset, many=True)
        return Response(serializer.data)
