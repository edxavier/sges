from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from mods.catalogs.serializers import ServiceSerializer, ItemSerializer
from .models import Incident, Severity, IncidentCategory, IncidentEntry, IncidentStatus, \
    KnownErrors, Task, TaskEntry, TaskType, Change, ChangeStatus, ChangeEntry, IncidentSource

class SeveritySerializer(ModelSerializer):
    class Meta:
        model = Severity
        fields = ['id', 'name', 'description']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = IncidentCategory
        fields = ['id', 'name']

class IncidentStatusSerializer(ModelSerializer):
    class Meta:
        model = IncidentStatus
        fields = ['id', 'name']

class ChangetStatusSerializer(ModelSerializer):
    class Meta:
        model = IncidentStatus
        fields = ['id', 'name']


class TaskTypeSerializer(ModelSerializer):
    class Meta:
        model = IncidentStatus
        fields = ['id', 'name']


class IncidentSourceSerializer(ModelSerializer):
    class Meta:
        model = IncidentSource
        fields = ['id', 'name']


class IncidentEntrySerializer(ModelSerializer):
    created_by_user = serializers.ReadOnlyField(source='created_by.full_name')
    _affected_services = ServiceSerializer(read_only=True, many=True, source='affected_services')
    _affected_items = ItemSerializer(read_only=True, many=True, source='affected_items')


    class Meta:
        model = IncidentEntry
        fields = '__all__'

class TaskEntrySerializer(ModelSerializer):
    created_by_user = serializers.ReadOnlyField(source='created_by.full_name')
    _affected_services = ServiceSerializer(read_only=True, many=True, source='affected_services')
    _affected_items = ItemSerializer(read_only=True, many=True, source='affected_items')


    class Meta:
        model = TaskEntry
        fields = '__all__'

class ChangeEntrySerializer(ModelSerializer):
    created_by_user = serializers.ReadOnlyField(source='created_by.full_name')
    _affected_services = ServiceSerializer(read_only=True, many=True, source='affected_services')
    _affected_items = ItemSerializer(read_only=True, many=True, source='affected_items')


    class Meta:
        model = ChangeEntry
        fields = '__all__'

class TaskSerializer(ModelSerializer):
    created_by_user = serializers.ReadOnlyField(source='created_by.full_name')
    updated_by_user = serializers.ReadOnlyField(source='updated_by.full_name')
    task_entries = TaskEntrySerializer(many=True, read_only=True)
    type_name = serializers.ReadOnlyField(source='type.name')
    status_name = serializers.ReadOnlyField(source='task_status.name')

    class Meta:
        model = Task
        fields = '__all__'

class ChangeSerializer(ModelSerializer):
    created_by_user = serializers.ReadOnlyField(source='created_by.full_name')
    updated_by_user = serializers.ReadOnlyField(source='updated_by.full_name')
    change_entries = ChangeEntrySerializer(many=True, read_only=True)
    status_name = serializers.ReadOnlyField(source='change_status.name')

    class Meta:
        model = Change
        fields = '__all__'

class IncidentSerializer(ModelSerializer):
    severity_name = serializers.ReadOnlyField(source='severity.name')
    created_by_user = serializers.ReadOnlyField(source='created_by.full_name')
    updated_by_user = serializers.ReadOnlyField(source='updated_by.full_name')
    category_name = serializers.ReadOnlyField(source='category.name')
    status_name = serializers.ReadOnlyField(source='status.name')
    source_name = serializers.ReadOnlyField(source='source.name')
    incident_entries = IncidentEntrySerializer(many=True, read_only=True)

    class Meta:
        model = Incident
        fields = '__all__'


class WorkaroundSerializer(ModelSerializer):
    created_by_user = serializers.ReadOnlyField(source='created_by.full_name')
    updated_by_user = serializers.ReadOnlyField(source='updated_by.full_name')

    class Meta:
        model = KnownErrors
        fields = '__all__'
