from rest_framework.response import Response
from rest_framework import viewsets
from .models import Class
from .serializer import ClassHistorySerializer, ClassSerializer
from django.db import models


class ClassViewset(viewsets.ModelViewSet):
    serializer_class = ClassSerializer

    def get_queryset(self):
        interface_id = self.request.query_params.get('InterfaceId')
        if interface_id:
            queryset = Class.objects.filter(InterfaceId_id=interface_id)
        else:
            queryset = Class.objects.all()
        return queryset


class ClassHistoryViewset(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Class.history.filter(Code=pk)
        serializer = ClassHistorySerializer(queryset, many=True)
        return Response(serializer.data)


class ClassDropdownViewset(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Class.objects.filter(Code=pk)
        foreign_key_fields = [field for field in Class._meta.get_fields() if isinstance(field, models.ForeignKey)]
        foreign_key_names = [
            str(field).split(":")[1].strip().split(">")[0].strip()
            if ":" in str(field) else str(field)
            for field in foreign_key_fields
        ]
        excluded_fields = ['created_by', 'updated_by']
        serializer = ClassSerializer(queryset, many=True)
        extracted_data = {field.split('.')[-1]: item[field.split('.')[-1]] for item in serializer.data for field in
                          foreign_key_names if field.split('.')[-1] not in excluded_fields}
        return Response(extracted_data)
