from django.shortcuts import render
from rest_framework import viewsets
from .models import Rol, Matrix, EmployeRol, Employe
from .serializers import RolSerializer, MatrixSerializer, EmployeRolSerializer
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from shared.Helpers import get_rol_index, get_rol_at_index
from datetime import date, timedelta

class RolViewSet(viewsets.ModelViewSet):

    authentication_classes = []
    permission_classes = []
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


class MatrixViewSet(viewsets.ModelViewSet):

    authentication_classes = []
    permission_classes = []
    queryset = Matrix.objects.all().order_by('index')
    serializer_class = MatrixSerializer

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = MatrixSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        pass


class EmployeRolViewSet(viewsets.ModelViewSet):

    authentication_classes = []
    permission_classes = []
    queryset = EmployeRol.objects.all()
    serializer_class = EmployeRolSerializer

    def create(self, request,  *args, **kwargs):
        try:
            employes = Employe.objects.filter(active=True).order_by('order') #Obtener los empleados
            matrix = Matrix.objects.filter(active=True).order_by('index') #Obtener la matriz
            total_weeks = 33  # simular el rol para 13 semanas en el futuro a partir de la fecha en que termino el rol anterior
            rol_weeks = request.data['weeks']  # numero de semanas que seran efectivas el resto 9 semanas teoricas
            if(rol_weeks< 4 and rol_weeks > 5):
                return Response({}, status=status.HTTP_400_BAD_REQUEST)
            # recorres la lista de 8 emps
            for employe in employes:
                current_date = employe.rol_end  # obtener la fecha en que termina el rol}
                EmployeRol.objects.filter(employe=employe).delete()  # Vaciar lista de horario antigua
                print(employe)
                last_rol = employe.last_rol
                # generar el Rol para determinado numero de semanas
                for week in range(1, total_weeks):
                    print('week:' + str(week))
                    #print('last_rol' + str(last_rol))
                    index = get_rol_index(matrix, last_rol.id)
                    # pasar al siguiente rol o volver al primero
                    if index < matrix.count()-1:
                        index = index + 1
                    else:
                        index = 0
                    rol = get_rol_at_index(matrix, index)
                    employeRol = EmployeRol()
                    employeRol.employe = employe
                    employeRol.rol = rol
                    dates = []
                    # range(desde , hasta -1)
                    for dia in range(1, 8):
                        current_date = current_date + timedelta(days=1)
                        dates.append(current_date)
                    employeRol.dates = dates
                    employeRol.save()
                    last_rol = rol

                    if week == rol_weeks:
                        employe.last_rol = last_rol
                        employe.valid_weeks = rol_weeks
                        employe.rol_end = current_date
                        employe.save()
                        print('Last Rol------- ' + str(last_rol))
                        print('Week------- ' + str(rol_weeks))
                        print('End at------- ' + str(current_date))
            return Response({}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
