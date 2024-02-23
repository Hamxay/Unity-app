from rest_framework import serializers

from connection.serializer import ConnectionDisplaySerializer
from schedule.serializer import ScheduleDisplaySerializer
from .models import InterfaceCategory, InterfaceType, Interface, InterfaceDependence


class InterfaceCategoryDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = InterfaceCategory
        fields = ['code', 'name']


class InterfaceDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Interface
        fields = ['code', 'name']


class InterfaceTypeDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = InterfaceType
        fields = ['code', 'name']


class InterfaceCategorySerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    updated_by = serializers.ReadOnlyField(source="created_by.get_full_name")

    class Meta:
        model = InterfaceCategory
        fields = "__all__"


class InterfaceTypeSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    updated_by = serializers.ReadOnlyField(source="created_by.get_full_name")

    class Meta:
        model = InterfaceType
        fields = "__all__"


class InterfaceSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    updated_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    interface_category_id = InterfaceCategoryDisplaySerializer()
    interface_type_id = InterfaceTypeDisplaySerializer()
    schedule_id = ScheduleDisplaySerializer()
    connection_id = ConnectionDisplaySerializer()

    class Meta:
        model = Interface
        fields = "__all__"


class InterfaceHistorySerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    updated_by = serializers.ReadOnlyField(source="created_by.get_full_name")

    class Meta:
        model = Interface.history.model
        fields = "__all__"


class InterfaceDependenceSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    updated_by = serializers.ReadOnlyField(source="created_by.get_full_name")
    interface_id = InterfaceDisplaySerializer()

    class Meta:
        model = InterfaceDependence
        fields = "__all__"
