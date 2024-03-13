import datetime
import math

import pandas as pd
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import redirect
from .models import Interface, Class

import pandas as pd
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Class
from interface.models import Interface
from django.utils import timezone


def import_class_from_file(file, current_user, success_url, request):
    if file.name.endswith(('.xlsx', '.xls')):
        if file.name.endswith('.xlsx'):
            df = pd.read_excel(file, engine='openpyxl')
        else:  # .xls file
            df = pd.read_excel(file, engine='xlrd')
    elif file.name.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        messages.error(request, "Unsupported file format. Only Excel files (.xlsx, .xls) and CSV files are supported.")
        return redirect(success_url)

    try:
        with transaction.atomic():
            for _, row in df.iterrows():
                interface_id = row['InterfaceId']
                try:
                    interface_instance = get_object_or_404(Interface, pk=int(interface_id))
                except (ValueError, TypeError):
                    raise ValidationError(f"Invalid classID \'{interface_id}\',  It should be a number.")
                class_id = row.get('Code')
                if not math.isnan(class_id):
                    try:
                        record_to_update = Class.objects.get(Code=class_id)
                        record_to_update.InterfaceId = interface_instance
                        record_to_update.created_by = current_user
                        record_to_update.updated_by = current_user
                        for key, value in row.items():
                            if key != 'InterfaceId':
                                setattr(record_to_update, key, value)
                        record_to_update.full_clean()
                        record_to_update.save()
                    except Class.DoesNotExist:
                        raise ValidationError(f"No attribute found with code: {class_id}")
                    except Exception as e:
                        messages.error(request=request, message=str(e))
                        raise ValidationError("An error occurred during import. Transaction rolled back.")
                else:
                    try:
                        class_instance = Class(
                            InterfaceId=interface_instance,
                            created_by=current_user,
                            updated_by=current_user,
                            **row.drop(['InterfaceId', 'Code']).to_dict()
                        )
                        class_instance.full_clean()
                        class_instance.save()
                    except Exception as e:
                        messages.error(request=request, message=str(e))

            messages.success(request, "Class(es) imported successfully")
    except ValidationError as errors:
        for error in errors:
            messages.error(request, error)
    except (TypeError, AttributeError, ValueError, Exception) as error:
        messages.error(request, str(error))

    return redirect(success_url)
