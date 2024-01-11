from django.dispatch import receiver
from simple_history.signals import (
    pre_create_historical_record,
)

from historyconfiguration.helper import history_enable


@receiver(pre_create_historical_record)
def pre_create_historical_record_callback(sender, instance, **kwargs):
    original_model_name = instance.__class__.__name__
    if history_enable(original_model_name):
        if hasattr(instance, "deleted_by") and instance.deleted_by is not None:
            kwargs["history_instance"].deleted_by = instance.deleted_by
        if hasattr(instance, "deleted_date") and instance.deleted_date is not None:
            kwargs["history_instance"].deleted_date = instance.deleted_date
    else:
        kwargs["history_instance"].skip_save = True
