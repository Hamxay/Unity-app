from rest_framework.response import Response
from rest_framework import viewsets
from .models import Collection
from .serializer import CollectionHistorySerializer, CollectionSerializer
from django.db import models


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
    def retrieve(self, request, code=None):
        queryset = Collection.history.filter(code=code)
        serializer = CollectionHistorySerializer(queryset, many=True)
        return Response(serializer.data)


class CollectionRelationsViewset(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Collection.objects.filter(code=pk)
        foreign_key_fields = [field for field in Collection._meta.get_fields() if isinstance(field, models.ForeignKey)]
        foreign_key_names = [
            str(field).split(":")[1].strip().split(">")[0].strip()
            if ":" in str(field) else str(field)
            for field in foreign_key_fields
        ]
        excluded_fields = ['created_by', 'updated_by']
        serializer = CollectionSerializer(queryset, many=True)
        extracted_data = {field.split('.')[-1]: item[field.split('.')[-1]] for item in serializer.data for field in
                          foreign_key_names if field.split('.')[-1] not in excluded_fields}
        return Response(extracted_data)
    