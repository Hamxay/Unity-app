from rest_framework import viewsets
from .models import APIIngestionBatchStatusLog, CheckpointLog, AuditLog, RunLog, RunStepLog
from .serializer import (
    APIIngestionBatchStatusLogSerializer,
    CheckpointLogSerializer,
    AuditLogSerializer,
    RunLogSerializer,
    RunStepLogSerializer
)


class APIIngestionBatchStatusLogListViewset(viewsets.ModelViewSet):
    queryset = APIIngestionBatchStatusLog.objects.all()
    serializer_class = APIIngestionBatchStatusLogSerializer


class CheckpointLogListViewset(viewsets.ModelViewSet):
    queryset = CheckpointLog.objects.all()
    serializer_class = CheckpointLogSerializer


class AuditLogListViewset(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer


class RunLogListViewset(viewsets.ModelViewSet):
    queryset = RunLog.objects.all()
    serializer_class = RunLogSerializer


class RunStepLogListViewset(viewsets.ModelViewSet):
    queryset = RunStepLog.objects.all()
    serializer_class = RunStepLogSerializer
