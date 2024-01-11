from rest_framework import serializers
from .models import KPI, KPIGroup, KPISubGroup


class KPIGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = KPIGroup
        fields = "__all__"


class KPISubGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = KPISubGroup
        fields = "__all__"


class KPISerializer(serializers.ModelSerializer):
    class Meta:
        model = KPI
        fields = "__all__"
