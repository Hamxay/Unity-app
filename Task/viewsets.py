from django.db.models import Q
from rest_framework.response import Response
from rest_framework import viewsets
from Task.models import Task
from Task.serializer import TaskHistorySerializer, TaskSerializer
from django.db import models


class TaskViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        collection_id = self.request.query_params.get('CollectionId')
        class_id = self.request.query_params.get('class_id')
        LoadPatternId = self.request.query_params.get('LoadPatternId')
        if collection_id:
            queryset = Task.objects.filter(CollectionId_id=collection_id)
        elif class_id:
            queryset = Task.objects.filter(ClassId_id=class_id)
        elif LoadPatternId:
            queryset = Task.objects.filter(LoadPatternId_id=LoadPatternId)
        else:
            queryset = Task.objects.all()
        return queryset


class TaskHistoryViewsetAll(viewsets.ReadOnlyModelViewSet):
    queryset = Task.history.all()
    serializer_class = TaskHistorySerializer


class TaskHistoryViewset(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Task.history.filter(Code=pk)
        serializer = TaskHistorySerializer(queryset, many=True)
        return Response(serializer.data)


class TaskDropdownViewset(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Task.objects.filter(Code=pk)
        foreign_key_fields = [field for field in Task._meta.get_fields() if isinstance(field, models.ForeignKey)]
        foreign_key_names = [
            str(field).split(":")[1].strip().split(">")[0].strip()
            if ":" in str(field) else str(field)
            for field in foreign_key_fields
        ]
        excluded_fields = ['created_by', 'updated_by']
        serializer = TaskSerializer(queryset, many=True)
        extracted_data = {field.split('.')[-1]: item[field.split('.')[-1]] for item in serializer.data for field in
                          foreign_key_names if field.split('.')[-1] not in excluded_fields}
        return Response(extracted_data)
