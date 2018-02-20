from .models import Rol, Matrix, EmployeRol, Employe
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class RolSerializer(ModelSerializer):
    class Meta:
        model = Rol
        exclude = ['description', ]


class EmployeSerializer(ModelSerializer):
    class Meta:
        model = Employe
        exclude = ['last_rol', 'active', 'rol_end']


class MatrixSerializer(ModelSerializer):
    monday_name = serializers.ReadOnlyField(source='monday.name')
    tuesday_name = serializers.ReadOnlyField(source='tuesday.name')
    wednesday_name = serializers.ReadOnlyField(source='wednesday.name')
    thursday_name = serializers.ReadOnlyField(source='thursday.name')
    friday_name = serializers.ReadOnlyField(source='friday.name')
    saturday_name = serializers.ReadOnlyField(source='saturday.name')
    sunday_name = serializers.ReadOnlyField(source='sunday.name')

    class Meta:
        model = Matrix
        fields = ('__all__')

class MatrixSerializer2(ModelSerializer):

    monday_name = serializers.ReadOnlyField(source='monday.name')
    tuesday_name = serializers.ReadOnlyField(source='tuesday.name')
    wednesday_name = serializers.ReadOnlyField(source='wednesday.name')
    thursday_name = serializers.ReadOnlyField(source='thursday.name')
    friday_name = serializers.ReadOnlyField(source='friday.name')
    saturday_name = serializers.ReadOnlyField(source='saturday.name')
    sunday_name = serializers.ReadOnlyField(source='sunday.name')

    class Meta:
        model = Matrix
        exclude = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', ]



class EmployeRolSerializer(ModelSerializer):

    employe = EmployeSerializer()
    rol = MatrixSerializer2()

    class Meta:
        model = EmployeRol
        fields = '__all__'
        depth = 2