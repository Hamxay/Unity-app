import pandas as pd
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
        messages.error(request, "Unsupported file format")
        return redirect(success_url)

    try:
        for _, row in df.iterrows():
            class_id = row['ClassId']
            collection_id = row['CollectionId']
            load_pattern_id = row['LoadPatternId']
            try:
                class_instance = get_object_or_404(Class, pk=int(class_id))
                collection_instance = get_object_or_404(Collection, pk=int(collection_id))
                load_pattern_instance = get_object_or_404(LoadPattern, pk=int(load_pattern_id))
            except (ValueError, TypeError):
                messages.error(request, "Invalid ID(s). They should be numbers.")
                return redirect(success_url)

            if row.get('Code') and isinstance(row['Code'], int):
                try:
                    task_instance = Task.objects.get(Code=row['Code'])
                    task_instance.ClassId = class_instance
                    task_instance.CollectionId = collection_instance
                    task_instance.LoadPatternId = load_pattern_instance
                    task_instance.created_by = current_user
                    task_instance.updated_by = current_user
                    for key, value in row.items():
                        if key != 'ClassId' and key != 'CollectionId' and key != 'LoadPatternId':  # Exclude IDs as they're already updated
                            setattr(task_instance, key, value)
                    task_instance.full_clean()
                    task_instance.save()
                except Task.DoesNotExist:
                    messages.error(request=request, message=f"No task found with code: {row['Code']}")
                except Exception as e:
                    messages.error(request=request, message=str(e))
            else:
                # Create a new task record if 'Code' is not provided
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

    except ValidationError as e:
        for field, errors in e.message_dict.items():
            for error in errors:
                messages.error(request, f"Error in field '{field}': {error}")
    except (TypeError, AttributeError, ValueError, Exception) as error:
        messages.error(request, str(error))
        return redirect(success_url)

    return redirect(success_url)