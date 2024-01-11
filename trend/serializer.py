from rest_framework import serializers
from .models import Trend, TrendCriteria


class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trend
        fields = "__all__"


class TrendCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendCriteria
        fields = "__all__"
