from rest_framework.response import Response
from rest_framework import viewsets
from .models import Class
from .serializer import ClassHistorySerializer, ClassSerializer


class ClassViewset(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassHistoryViewset(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Class.history.filter(id=pk)
        serializer = ClassHistorySerializer(queryset, many=True)
        return Response(serializer.data)
