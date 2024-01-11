from rest_framework.response import Response
from rest_framework import viewsets
from .models import Connection
from .serializer import ConnectionHistorySerializer, ConnectionSerializer


class ConnectionViewset(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer


class ConnectionHistoryViewset(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Connection.history.filter(id=pk)
        serializer = ConnectionHistorySerializer(queryset, many=True)
        return Response(serializer.data)
