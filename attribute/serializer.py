from rest_framework import serializers

from classapp.serializer import ClassDisplaySerializer
from .models import Attribute


class AttributeSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    updated_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    class_id = ClassDisplaySerializer()

    class Meta:
        model = Attribute
        fields = "__all__"


class AttributeHistorySerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    updated_by = serializers.ReadOnlyField(source="created_by.get_full_name")

    class Meta:
        model = Attribute.history.model
        fields = "__all__"
