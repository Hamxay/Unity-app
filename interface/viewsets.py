from django.db import models
from rest_framework.response import Response
from rest_framework import viewsets
from .models import InterfaceCategory, InterfaceType, Interface, InterfaceDependence
from .serializer import (
    InterfaceCategorySerializer,
    InterfaceTypeSerializer,
    InterfaceSerializer,
    InterfaceDependenceSerializer,
    InterfaceHistorySerializer,
)


class InterfaceCategoryViewset(viewsets.ModelViewSet):
    queryset = InterfaceCategory.objects.all()
    serializer_class = InterfaceCategorySerializer


class InterfaceTypeViewset(viewsets.ModelViewSet):
    queryset = InterfaceType.objects.all()
    serializer_class = InterfaceTypeSerializer


class InterfaceViewset(viewsets.ModelViewSet):
    queryset = Interface.objects.all()
    serializer_class = InterfaceSerializer


class InterfaceHistoryViewset(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Interface.history.filter(id=pk)
        serializer = InterfaceHistorySerializer(queryset, many=True)
        return Response(serializer.data)


class InterfaceDependenceViewset(viewsets.ModelViewSet):
    queryset = InterfaceDependence.objects.all()
    serializer_class = InterfaceDependenceSerializer


class InterfaceDropdownViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Interface.objects.filter(id=pk)
        foreign_key_fields = [field for field in Interface._meta.get_fields() if isinstance(field, models.ForeignKey)]
        foreign_key_names = [
            str(field).split(":")[1].strip().split(">")[0].strip()
            if ":" in str(field) else str(field)
            for field in foreign_key_fields
        ]
        excluded_fields = ['created_by', 'updated_by']
        serializer = InterfaceSerializer(queryset, many=True)
        extracted_data = {field.split('.')[-1]: item[field.split('.')[-1]] for item in serializer.data for field in
                          foreign_key_names if field.split('.')[-1] not in excluded_fields}
        return Response(extracted_data)


