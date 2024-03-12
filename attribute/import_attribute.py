import pandas as pd
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
        messages.error(request, "Unsupported file format")
        return redirect(success_url)

    try:
        for _, row in df.iterrows():
            class_id = row['class_id']
            try:
                class_instance = get_object_or_404(Class, pk=int(class_id))
            except (ValueError, TypeError):
                messages.error(request, f"Invalid classID {class_id},  It should be a number.")
                return redirect(success_url)

            if row.get('code') and isinstance(row['code'], int):
                try:
                    attribute_instance = Attribute.objects.get(code=row['code'])
                    attribute_instance.class_id = class_instance
                    attribute_instance.created_by = current_user
                    attribute_instance.updated_by = current_user
                    for key, value in row.items():
                        if key != 'class_id':  # Exclude class_id as it's already updated
                            setattr(attribute_instance, key, value)
                    attribute_instance.full_clean()
                    attribute_instance.save()
                except Attribute.DoesNotExist:
                    messages.error(request=request, message=f"No attribute found with code: {row['code']}")
                except Exception as e:
                    messages.error(request=request, message=str(e))
            else:
                # Create a new attribute record if 'code' is not provided
                attribute_instance = Attribute(
                    class_id=class_instance,
                    created_by=current_user,
                    updated_by=current_user,
                    **row.drop(['class_id', 'code']).to_dict()
                )
                attribute_instance.full_clean()
                attribute_instance.save()

        messages.success(request, "Attribute(s) imported successfully")

    except ValidationError as e:
        for field, errors in e.message_dict.items():
            for error in errors:
                messages.error(request, f"Error in field '{field}': {error}")
    except (TypeError, AttributeError, ValueError, Exception) as error:
        messages.error(request, str(error))
        return redirect(success_url)

    return redirect(success_url)
