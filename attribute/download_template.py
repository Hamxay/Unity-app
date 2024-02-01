import csv
from django.http import HttpResponse


class AttributeTemplateCSVGenerator:
    @staticmethod
    def generate_csv():
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="AttributeTemplate.csv"'
        csv_writer = csv.writer(response)
        csv_writer.writerow([
            "class_id", "source_name", "target_name", "source_description", "target_description",
            "source_ordinal_position", "target_ordinal_position", "source_data_type", "target_data_type",
            "source_max_length", "target_max_length", "source_precision", "target_precision",
            "source_scale", "target_scale", "is_primary_key", "is_snapshot_key", "is_nullable",
            "ignore_on_ingest",
            # "history",
            "created_by", "updated_by", "created_date", "updated_date"
        ])

        csv_writer.writerow([
            "1",   # class_id - Assuming the first Class instance has ID 1
            "Default source_name", "Default target_name", "Default source_description", "Default target_description",
            "1",  # source_ordinal_position
            "1",  # target_ordinal_position
            "Default source_data_type", "Default target_data_type",
            "1",  # source_max_length
            "1",  # target_max_length
            "1",  # source_precision
            "1",  # target_precision
            "1",  # source_scale
            "1",  # target_scale
            "False",  # is_primary_key
            "False",  # is_snapshot_key
            "False",  # is_nullable
            "False",  # ignore_on_ingest
            # "History data",  # history
            "1",  # created_by_id
            "1",  # updated_by_id
            "2024-01-30T12:00:00Z",
            "2024-01-30T12:00:00Z"
        ])

        return response
