from rest_framework import serializers
from .models import LoadPattern


class LoadPatternSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    updated_by = serializers.ReadOnlyField(source="created_by.get_full_name")

    class Meta:
        model = LoadPattern
        fields = "__all__"


class LoadPatternDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadPattern
        fields = ['code', 'name']
