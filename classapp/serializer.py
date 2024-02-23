from rest_framework import serializers

from interface.serializer import InterfaceDisplaySerializer
from .models import Class


class ClassSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    updated_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    InterfaceId = InterfaceDisplaySerializer()

    class Meta:
        model = Class
        fields = "__all__"


class ClassHistorySerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    updated_by = serializers.ReadOnlyField(source="created_by.get_full_name")

    class Meta:
        model = Class.history.model
        fields = "__all__"


class ClassDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['Code', 'Name']
