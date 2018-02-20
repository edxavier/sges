from django.contrib.auth.models import Group, Permission, ContentType
from .models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


"""Serializer para el payload del JWT"""
class UserDetailSerializer(ModelSerializer):
    #username = serializers.CharField(required=False)
    _full_name = serializers.CharField(source='full_name')

    class Meta:
        model = User
        exclude = ('password', 'last_login', 'date_joined')
        depth = 3


"""Serializer para Listar los usuarios sin tanto detalle"""
class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'last_login', 'date_joined', 'groups', 'user_permissions')
        depth = 0


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class ContentTypeSerializer(ModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'


class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
        #fields = ('id', 'name', 'codename')