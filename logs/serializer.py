from .models import APIIngestionBatchStatusLog,CheckpointLog,AuditLog,RunLog,RunStepLog
from rest_framework import serializers


class APIIngestionBatchStatusLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIIngestionBatchStatusLog
        fields = "__all__"


class CheckpointLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckpointLog
        fields = "__all__"


class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = "__all__"


class RunLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunLog
        fields = "__all__"


class RunStepLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunStepLog
        fields = "__all__"
