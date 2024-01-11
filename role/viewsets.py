from rest_framework import viewsets
from .models import Role
from .serializer import RoleSerializer


class RoleViewset(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
