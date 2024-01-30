from django.db import models
from rest_framework.response import Response
from rest_framework import viewsets
from django.db.models import Q
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
    serializer_class = InterfaceSerializer

    def get_queryset(self):
        connection_id = self.request.query_params.get('ConnectionId')
        interface_category_id = self.request.query_params.get('InterfaceCategoryId')
        load_patterns_id = self.request.query_params.get('LoadPatternId')
        if connection_id:
            queryset = Interface.objects.filter(connection_id_id=connection_id)
        elif interface_category_id:
            queryset = Interface.objects.filter(interface_category_id_id=interface_category_id)
        # elif load_patterns_id:
        #     queryset = Interface.objects.filter(load_patterns_id_id=load_patterns_id)
        else:
            queryset = Interface.objects.all()
        return queryset


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
        queryset = Interface.objects.filter(code=pk)
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


class InterfaceTypeDetailViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = InterfaceType.objects.filter(code=pk)
        foreign_key_fields = [
            field for field in InterfaceType._meta.get_fields() if isinstance(field, models.ForeignKey)
        ]
        foreign_key_names = [
            str(field).split(":")[1].strip().split(">")[0].strip()
            if ":" in str(field) else str(field)
            for field in foreign_key_fields
        ]
        excluded_fields = ['created_by', 'updated_by']
        serializer = InterfaceTypeSerializer(queryset, many=True)
        extracted_data = {field.split('.')[-1]: item[field.split('.')[-1]] for item in serializer.data for field in
                          foreign_key_names if field.split('.')[-1] not in excluded_fields}
        return Response(extracted_data)


