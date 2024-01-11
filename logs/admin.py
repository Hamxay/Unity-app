from django.contrib import admin
from logs.models import APIIngestionBatchStatusLog,CheckpointLog,AuditLog,RunLog,RunStepLog

admin.site.register(APIIngestionBatchStatusLog)
admin.site.register(CheckpointLog)
admin.site.register(AuditLog)
admin.site.register(RunLog)
admin.site.register(RunStepLog)
