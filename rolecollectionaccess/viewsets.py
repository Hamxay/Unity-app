from rest_framework import viewsets
from .models import RoleCollectionAccess
from .serializer import RoleCollectionAccessSerializer


class RoleCollectionAccessViewset(viewsets.ModelViewSet):
    queryset = RoleCollectionAccess.objects.all()
    serializer_class = RoleCollectionAccessSerializer
