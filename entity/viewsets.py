from rest_framework import viewsets
from .models import Entity
from .serializer import EntitySerializer


class EntityViewset(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
