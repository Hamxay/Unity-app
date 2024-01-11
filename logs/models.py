from django.db import models
from interface.models import Interface
from collection.models import Collection


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_date"]


class APIIngestionBatchStatusLog(BaseModel):
    meta_load_dt = models.DateTimeField()
    meta_run_step_log_id = models.IntegerField()
    class_id = models.IntegerField()
    class_name = models.CharField(max_length=200, null=True)
    batch_id = models.IntegerField()
    batch_filter = models.TextField(null=True)
    batch_stg_file_add_field_value = models.TextField(null=True)
    api_extract_status_id = models.IntegerField(null=True)
    api_extract_run_start_dt = models.DateTimeField(null=True)
    api_extract_run_end_dt = models.DateTimeField(null=True)
    api_extract_error_message = models.TextField(null=True)
    convert_json_to_stg_file_has_error = models.BooleanField(null=True)
    convert_json_to_stg_file_error_message = models.TextField(null=True)

    class Meta:
        db_table = (
            "APIIngestionBatchStatusLog"  # Set the table name to match the SQL table
        )

    def __str__(self):
        return f"APIIngestionBatchStatusLog ID: {self.id}"


class CheckpointLog(BaseModel):
    interface_id = models.IntegerField()
    task_id = models.IntegerField()
    task_load_date = models.DateTimeField()
    activity_name = models.CharField(max_length=128)
    activity_status = models.CharField(max_length=50)
    activity_run_start_time = models.DateTimeField()
    activity_run_end_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'CheckpointLog'


class AuditLog(BaseModel):
    run_step_log_id = models.IntegerField()
    class_id = models.IntegerField()
    class_name = models.CharField(max_length=128)
    stage_row_count = models.IntegerField(null=True)
    insert_row_count = models.IntegerField(null=True)
    update_row_count = models.IntegerField(null=True)
    delete_row_count = models.IntegerField(null=True)

    class Meta:
        db_table = 'AuditLog'


class RunLog(BaseModel):
    InterfaceId = models.ForeignKey(Interface, on_delete=models.CASCADE)
    StatusId = models.IntegerField(null=False)
    execution_date = models.DateTimeField(auto_now=True)
    run_type = models.CharField(max_length=30)
    start_time = models.DateTimeField(null=True, blank=True, auto_now=True)
    end_time = models.DateTimeField(null=True, blank=True, auto_now=True)
    is_rerun = models.CharField(max_length=1)
    time_to_live = models.DateTimeField(auto_now=True)
    interface_pipeline_run_id = models.CharField(max_length=50, null=True, blank=True)
    scheduler_pipeline_run_id = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'RunLog'


class RunStepLog(BaseModel):
    run_log_id = models.ForeignKey(RunLog, on_delete=models.CASCADE)
    status_id = models.IntegerField()
    task_id = models.IntegerField()
    collection_id = models.ForeignKey(Collection, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    collection_pipeline_run_id = models.CharField(max_length=50, null=True, blank=True)
    task_pipeline_run_id = models.CharField(max_length=50, null=True, blank=True)
    error = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'RunStepLog'
