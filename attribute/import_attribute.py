import math

import pandas as pd
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import redirect
from .models import Class, Attribute


def import_attributes_from_file(file, current_user, success_url, request):
    if file.name.endswith(('.xlsx', '.xls')):
        if file.name.endswith('.xlsx'):
            df = pd.read_excel(file, engine='openpyxl')
        else:  # .xls file
            df = pd.read_excel(file, engine='xlrd')
    elif file.name.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        messages.error(request, "Unable to import data (Attribute) from the file. Only csv, xlsx and xls files are "
                                "supported")
        return redirect(success_url)

    try:
        with transaction.atomic():
            for _, row in df.iterrows():
                class_id = row['class_id']
                try:
                    class_instance = get_object_or_404(Class, pk=int(class_id))
                except (ValueError, TypeError) as error:
                    raise ValidationError(f"Unable to import data (Attribute) from the file because `{error}`")

                if not math.isnan(row.get('code')):
                    try:
                        attribute_instance = Attribute.objects.get(code=row['code'])
                        attribute_instance.class_id = class_instance
                        attribute_instance.created_by = current_user
                        attribute_instance.updated_by = current_user
                        for key, value in row.items():
                            if key != 'class_id':
                                setattr(attribute_instance, key, value)
                        attribute_instance.full_clean()
                        attribute_instance.save()
                    except (Attribute.DoesNotExist, Exception) as error:
                        raise ValidationError(f"Unable to import data (Attribute) from the file because `{error}`")
                else:
                    attribute_instance = Attribute(
                        class_id=class_instance,
                        created_by=current_user,
                        updated_by=current_user,
                        **row.drop(['class_id', 'code']).to_dict()
                    )
                    attribute_instance.full_clean()
                    attribute_instance.save()

            messages.success(request, "Attribute(s) imported successfully")
    except ValidationError as errors:
        for error in errors:
            messages.error(request, error)

    except (TypeError, AttributeError, ValueError, Exception) as error:
        messages.error(request, f" Unable to import data (Attribute) because `{error}`")

    return redirect(success_url)
