from rest_framework.response import Response
from rest_framework import viewsets

from .filterset import AttributeFilterset
from .models import Attribute
from .serializer import AttributeHistorySerializer, AttributeSerializer


class AttributeViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        class_id = self.request.query_params.get('class_id')
        if class_id:
            queryset = Attribute.objects.filter(class_id_id=class_id)
        else:
            queryset = Attribute.objects.all()
        return queryset

    serializer_class = AttributeSerializer
    filterset_class = AttributeFilterset


class AttributeHistoryViewset(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Attribute.history.filter(code=pk)
        serializer = AttributeHistorySerializer(queryset, many=True)
        return Response(serializer.data)
