from rest_framework.response import Response
from rest_framework import viewsets
from .models import Attribute
from .serializer import AttributeHistorySerializer, AttributeSerializer


class AttributeViewset(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer


class AttributeHistoryViewset(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Attribute.history.filter(id=pk)
        serializer = AttributeHistorySerializer(queryset, many=True)
        return Response(serializer.data)
