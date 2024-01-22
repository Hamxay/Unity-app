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
        queryset = Interface.history.filter(id=pk)
        serializer = InterfaceHistorySerializer(queryset, many=True)
        return Response(serializer.data)
