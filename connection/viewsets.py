from rest_framework.response import Response
from rest_framework import viewsets
from .models import Connection
from .serializer import ConnectionHistorySerializer, ConnectionSerializer
from django.db import models


class ConnectionViewset(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer


class ConnectionHistoryViewset(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Connection.history.filter(code=pk)
        serializer = ConnectionHistorySerializer(queryset, many=True)
        return Response(serializer.data)


class ConnectionDropdownViewset(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Connection.objects.filter(code=pk)
        foreign_key_fields = [field for field in Connection._meta.get_fields() if isinstance(field, models.ForeignKey)]
        foreign_key_names = [
            str(field).split(":")[1].strip().split(">")[0].strip()
            if ":" in str(field) else str(field)
            for field in foreign_key_fields
        ]
        excluded_fields = ['created_by', 'updated_by']
        serializer = ConnectionSerializer(queryset, many=True)
        extracted_data = {field.split('.')[-1]: item[field.split('.')[-1]] for item in serializer.data for field in
                          foreign_key_names if field.split('.')[-1] not in excluded_fields}
        return Response(extracted_data)
