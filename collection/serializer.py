from rest_framework import serializers

from interface.serializer import InterfaceDisplaySerializer
from .models import Collection


class CollectionSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    updated_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    interfaceid = InterfaceDisplaySerializer()  # for multiple interface fields in collection_list

    class Meta:
        model = Collection
        fields = "__all__"


class CollectionHistorySerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    updated_by = serializers.ReadOnlyField(source="created_by.get_full_name")

    class Meta:
        model = Collection.history.model
        fields = "__all__"
