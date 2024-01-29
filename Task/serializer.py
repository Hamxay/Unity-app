
from rest_framework import serializers
from Task.models import Task
from classapp.serializer import ClassDisplaySerializer
from collection.serializer import CollectionsDisplaySerializer
from pattern.serializer import LoadPatternDisplaySerializer


class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    updated_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    ClassId = ClassDisplaySerializer()
    CollectionId = CollectionsDisplaySerializer()
    LoadPatternId = LoadPatternDisplaySerializer()

    class Meta:
        model = Task
        fields = "__all__"


class TaskHistorySerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    updated_by = serializers.ReadOnlyField(source="created_by.get_full_name")

    class Meta:
        model = Task.history.model
        fields = "__all__"
