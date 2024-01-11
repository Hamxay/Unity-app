from rest_framework import viewsets
from .models import KPI, KPIGroup, KPISubGroup
from .serializer import KPIGroupSerializer, KPISubGroupSerializer, KPISerializer


class KPIGroupViewset(viewsets.ModelViewSet):
    queryset = KPIGroup.objects.all()
    serializer_class = KPIGroupSerializer


class KPISubGroupViewset(viewsets.ModelViewSet):
    queryset = KPISubGroup.objects.all()
    serializer_class = KPISubGroupSerializer


class KPIViewset(viewsets.ModelViewSet):
    queryset = KPI.objects.all()
    serializer_class = KPISerializer
