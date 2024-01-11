from rest_framework import viewsets
from .models import Targets
from .serializer import TargetsSerializer


class TargetsViewset(viewsets.ModelViewSet):
    queryset = Targets.objects.all()
    serializer_class = TargetsSerializer
