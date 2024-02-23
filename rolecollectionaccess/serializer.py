from rest_framework import serializers

from collection.serializer import CollectionsDisplaySerializer
from role.serializer import RoleDisplaySerializer
from .models import RoleCollectionAccess


class RoleCollectionAccessSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    updated_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    collectionId = CollectionsDisplaySerializer()
    RoleId = RoleDisplaySerializer()

    class Meta:
        model = RoleCollectionAccess
        fields = "__all__"
