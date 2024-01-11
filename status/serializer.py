from rest_framework import serializers
from .models import StatusGroup, Status, StatusCriteria


class StatusGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusGroup
        fields = "__all__"


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"


class StatusCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusCriteria
        fields = "__all__"
