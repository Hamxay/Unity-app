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

            task_instance = Task(
                ClassId=class_instance,
                CollectionId=collection_instance,
                LoadPatternId=load_pattern_instance,
                created_by=current_user,
                updated_by=current_user,
                **row.drop(['ClassId', 'CollectionId', 'LoadPatternId',  'created_by', 'updated_by']).to_dict()
            )
            task_instance.full_clean()
            task_instance.save()

        messages.success(request, "Task(s) imported successfully")

    except ValidationError as e:
        for field, errors in e.message_dict.items():
            for error in errors:
                messages.error(request, f"Error in field '{field}': {error}")

    return redirect(success_url)
