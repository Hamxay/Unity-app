import csv
from django.http import HttpResponse


def generate_class_csv_template():
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ClassTemplate.csv"'
    csv_writer = csv.writer(response)
    csv_writer.writerow([
        "Code", "InterfaceId", "Name", "Description", "Prefix", "Version",
        "TargetAlias", "IgnoreOnIngest", "SlideWindowAttribute", "SlideWindowDays",
        "Mask", "Filter",
    ])
    csv_writer.writerow([
        "1",  # Code - Assuming the first class instance has Code 1
        "1",  # InterfaceId - Assuming the first Interface instance has ID 1
        "Default Name", "Default Description", "Default Prefix", "1",  # Version
        "Default TargetAlias", "False", "Default SlideWindowAttribute", "7",  # SlideWindowDays
        "Default Mask", "Default Filter",

    ])
    return response
