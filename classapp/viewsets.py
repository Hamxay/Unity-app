from rest_framework.response import Response
from rest_framework import viewsets
from .models import Class
from .serializer import ClassHistorySerializer, ClassSerializer


class ClassViewset(viewsets.ModelViewSet):
    serializer_class = ClassSerializer

    def get_queryset(self):
        interface_id = self.request.query_params.get('InterfaceId')
        if interface_id:
            queryset = Class.objects.filter(InterfaceId_id=interface_id)
        else:
            queryset = Class.objects.all()
        return queryset


class ClassHistoryViewset(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Class.history.filter(id=pk)
        serializer = ClassHistorySerializer(queryset, many=True)
        return Response(serializer.data)
