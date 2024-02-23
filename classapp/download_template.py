import csv
from django.http import HttpResponse


def generate_class_csv_template():
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ClassTemplate.csv"'
    csv_writer = csv.writer(response)
    csv_writer.writerow([
        "InterfaceId", "Name", "Description", "Prefix", "Version",
        "TargetAlias", "IgnoreOnIngest", "SlideWindowAttribute", "SlideWindowDays",
        "Mask", "Filter", "created_by", "updated_by", "created_date", "updated_date"
    ])
    csv_writer.writerow([
        "1",  # InterfaceId - Assuming the first Interface instance has ID 1
        "Default Name", "Default Description", "Default Prefix", "1",  # Version
        "Default TargetAlias", "False", "Default SlideWindowAttribute", "7",  # SlideWindowDays
        "Default Mask", "Default Filter",
        "1",  # created_by_id - Assuming the first User instance has ID 1
        "1",  # updated_by_id - Assuming the first User instance has ID 1
        "2024-01-30T12:00:00Z",
        "2024-01-30T12:00:00Z"
    ])
    return response
