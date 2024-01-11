from rest_framework import viewsets
from .models import LoadPattern
from .serializer import LoadPatternSerializer


class LoadPatternViewset(viewsets.ModelViewSet):
    queryset = LoadPattern.objects.all()
    serializer_class = LoadPatternSerializer
