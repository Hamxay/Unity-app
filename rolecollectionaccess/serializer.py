from rest_framework import serializers
from .models import RoleCollectionAccess


class RoleCollectionAccessSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    updated_by = serializers.ReadOnlyField(source="created_by.get_full_name")

    class Meta:
        model = RoleCollectionAccess
        fields = "__all__"
