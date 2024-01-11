from rest_framework import viewsets
from .models import StatusGroup, Status, StatusCriteria
from .serializer import (
    StatusGroupSerializer,
    StatusSerializer,
    StatusCriteriaSerializer,
)


class StatusGroupViewset(viewsets.ModelViewSet):
    queryset = StatusGroup.objects.all()
    serializer_class = StatusGroupSerializer


class StatusViewset(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusCriteriaViewset(viewsets.ModelViewSet):
    queryset = StatusCriteria.objects.all()
    serializer_class = StatusCriteriaSerializer
