from rest_framework.response import Response
from rest_framework import viewsets
from .models import Collection
from .serializer import CollectionHistorySerializer, CollectionSerializer


class CollectionViewset(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CollectionHistoryViewset(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Collection.history.filter(id=pk)
        serializer = CollectionHistorySerializer(queryset, many=True)
        return Response(serializer.data)
