import csv
from django.http import HttpResponse


def generate_task_csv_template():
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="TaskTemplate.csv"'
    csv_writer = csv.writer(response)
    csv_writer.writerow([
        "ClassId", "CollectionId", "LoadPatternId", "Name", "Description", "ProcessName", "ProcessParameters",
        "SubProcessParameters", "DeduplicateSource", "Priority", "created_by", "updated_by", "created_date",
        "updated_date"
    ])
    csv_writer.writerow([
        "1",  # ClassId - Assuming the first Class instance has ID 1
        "1",  # CollectionId - Assuming the first Interface instance has ID 1
        "1",  # LoadPatternId - Assuming the first Interface instance has ID 1
        "Default Name", "Default Description", "Default ProcessName", "ProcessParameters",
        "Default SubProcessParameters", "False", "7",  # Priority
        "1",  # created_by_id - Assuming the first User instance has ID 1
        "1",  # updated_by_id - Assuming the first User instance has ID 1
        "2024-01-30T12:00:00Z",
        "2024-01-30T12:00:00Z"
    ])
    return response
