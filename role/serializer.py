from rest_framework import serializers
from .models import Role


class RoleSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    updated_by = serializers.ReadOnlyField(source="created_by.get_full_name")

    class Meta:
        model = Role
        fields = "__all__"


class RoleDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['code', 'name']
