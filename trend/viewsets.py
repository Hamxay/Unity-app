from rest_framework import viewsets
from .models import Trend, TrendCriteria
from .serializer import TrendSerializer, TrendCriteriaSerializer


class TrendViewset(viewsets.ModelViewSet):
    queryset = Trend.objects.all()
    serializer_class = TrendSerializer


class TrendCriteriaViewset(viewsets.ModelViewSet):
    queryset = TrendCriteria.objects.all()
    serializer_class = TrendCriteriaSerializer
