from .models import Item, ItemHistory, Service, ItemType, ItemStatus, ServiceType, ServiceCategory, System, Location
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class ItemTypeSerializer(ModelSerializer):
    class Meta:
        model = ItemType
        fields = ['id', 'name']

class ItemStatusSerializer(ModelSerializer):
    class Meta:
        model = ItemStatus
        fields = ['id', 'name']

class ServiceTypeSerializer(ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ['id', 'name']


class ServiceCategorySerializer(ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ['id', 'name']


class SystemSerializer(ModelSerializer):
    class Meta:
        model = System
        fields = ['id', 'name']


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']



class ItemSerializer(ModelSerializer):
    type_name = serializers.ReadOnlyField(source='type.name')
    location_name = serializers.ReadOnlyField(source='location.name')
    system_name = serializers.ReadOnlyField(source='system.name')
    status_name = serializers.ReadOnlyField(source='status.name')

    class Meta:
        model = Item
        fields = '__all__'


class ServiceSerializer(ModelSerializer):
    type_name = serializers.ReadOnlyField(source='type.name')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Service
        fields = '__all__'


class ItemHistorySerializer(ModelSerializer):
    location_name = serializers.ReadOnlyField(source='location.name')
    status_name = serializers.ReadOnlyField(source='status.name')
    user = serializers.ReadOnlyField(source='created_by.full_name')

    class Meta:
        model = ItemHistory
        fields = '__all__'