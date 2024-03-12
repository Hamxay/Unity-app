import math

import pandas as pd
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import redirect
from .models import Class, Collection, LoadPattern, Task


def import_tasks_from_file(file, current_user, success_url, request):
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
                class_id = row['ClassId']
                collection_id = row['CollectionId']
                load_pattern_id = row['LoadPatternId']
                try:
                    class_instance = get_object_or_404(Class, pk=int(class_id))
                    collection_instance = get_object_or_404(Collection, pk=int(collection_id))
                    load_pattern_instance = get_object_or_404(LoadPattern, pk=int(load_pattern_id))
                except (ValueError, TypeError):
                    raise ValidationError(f"Invalid IDs, Every Id should be a valid integer.")

                if not math.isnan(row.get('code')):
                    try:
                        task_instance = Task.objects.get(Code=row['Code'])
                        task_instance.ClassId = class_instance
                        task_instance.CollectionId = collection_instance
                        task_instance.LoadPatternId = load_pattern_instance
                        task_instance.created_by = current_user
                        task_instance.updated_by = current_user
                        for key, value in row.items():
                            if key != 'ClassId' and key != 'CollectionId' and key != 'LoadPatternId':
                                setattr(task_instance, key, value)
                        task_instance.full_clean()
                        task_instance.save()
                    except Task.DoesNotExist:
                        raise ValidationError(f"No task found with code: {row['Code']}")
                    except Exception as e:
                        raise ValidationError("An error occurred during import. Transaction rolled back.")
                else:
                    task_instance = Task(
                        ClassId=class_instance,
                        CollectionId=collection_instance,
                        LoadPatternId=load_pattern_instance,
                        created_by=current_user,
                        updated_by=current_user,
                        **row.drop(['ClassId', 'CollectionId', 'LoadPatternId', 'Code']).to_dict()
                    )
                    task_instance.full_clean()
                    task_instance.save()

            messages.success(request, "Task(s) imported successfully")
    except ValidationError as errors:
        for error in errors:
            messages.error(request, error)
    except (TypeError, AttributeError, ValueError, Exception) as error:
        messages.error(request, str(error))

    return redirect(success_url)
