from rest_framework import serializers
from .models import Frequency


class FrequencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Frequency
        fields = "__all__"
