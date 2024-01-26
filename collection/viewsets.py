from rest_framework.response import Response
from rest_framework import viewsets
from .models import Collection
from .serializer import CollectionHistorySerializer, CollectionSerializer


class CollectionViewset(viewsets.ModelViewSet):
    serializer_class = CollectionSerializer

    def get_queryset(self):
        interface_id = self.request.query_params.get('InterfaceId')
        if interface_id:
            queryset = Collection.objects.filter(interfaceid_id=interface_id)
        else:
            queryset = Collection.objects.all()
        return queryset


class CollectionHistoryViewset(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Collection.history.filter(id=pk)
        serializer = CollectionHistorySerializer(queryset, many=True)
        return Response(serializer.data)
