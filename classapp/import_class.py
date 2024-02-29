import pandas as pd
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import redirect
from .models import Interface, Class


def import_class_from_file(file, current_user, success_url, request):
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
            interface_id = row['InterfaceId']
            try:
                interface_instance = get_object_or_404(Interface, pk=int(interface_id))
            except (ValueError, TypeError):
                messages.error(request, f"Invalid Interface ID: {interface_id}. It should be a number.")
                return redirect(success_url)

            class_instance = Class(
                InterfaceId=interface_instance,
                created_by=current_user,
                updated_by=current_user,
                **row.drop(['InterfaceId', 'Id',]).to_dict()
            )
            class_instance.full_clean()
            class_instance.save()

        messages.success(request, "Class(s) imported successfully")

    except ValidationError as e:
        for field, errors in e.message_dict.items():
            for error in errors:
                messages.error(request, f"Error in field '{field}': {error}")
    except (TypeError, AttributeError, ValueError, Exception) as error:
        messages.error(request, error)
        return redirect(success_url)
    return redirect(success_url)
