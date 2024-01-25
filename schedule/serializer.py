from rest_framework import serializers
from schedule.models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    updated_by = serializers.ReadOnlyField(source="created_by.get_full_name")

    class Meta:
        model = Schedule
        fields = "__all__"


class ScheduleHistorySerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    updated_by = serializers.ReadOnlyField(source="created_by.get_full_name")

    class Meta:
        model = Schedule.history.model
        fields = "__all__"


class ScheduleDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['Code', 'Name']
        