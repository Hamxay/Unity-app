from rest_framework.response import Response
from rest_framework import viewsets

from .filterset import AttributeFilterset
from .models import Attribute
from .serializer import AttributeHistorySerializer, AttributeSerializer


class AttributeViewset(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    filterset_class = AttributeFilterset


class AttributeHistoryViewset(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Attribute.history.filter(code=pk)
        serializer = AttributeHistorySerializer(queryset, many=True)
        return Response(serializer.data)