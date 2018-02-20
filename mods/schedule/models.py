from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Rol(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=20, default='')
    workin_hours = models.IntegerField(default=8)

    class Meta:
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.description


class Matrix(models.Model):

    index = models.IntegerField()
    monday = models.ForeignKey(Rol, related_name='monday', on_delete=models.CASCADE, verbose_name='Lunes')
    tuesday = models.ForeignKey(Rol, related_name='tuesday', on_delete=models.CASCADE, verbose_name='Martes')
    wednesday = models.ForeignKey(Rol, related_name='wednesday', on_delete=models.CASCADE, verbose_name='Miercoles')
    thursday = models.ForeignKey(Rol, related_name='thursday', on_delete=models.CASCADE, verbose_name='Jueves')
    friday = models.ForeignKey(Rol, related_name='friday', on_delete=models.CASCADE, verbose_name='Viernes')
    saturday = models.ForeignKey(Rol, related_name='saturday', on_delete=models.CASCADE, verbose_name='Sabado')
    sunday = models.ForeignKey(Rol, related_name='sunday', on_delete=models.CASCADE, verbose_name='Domingo')

    tasks = models.CharField(max_length=100, null=True, blank=True)
    total_hours = models.IntegerField(default=48)
    worked_hours = models.IntegerField(default=48)
    extras = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Rol Matriz'
        verbose_name_plural = 'Matriz'

    def __str__(self):
        return str(self.index) + ' | ' + self.monday.name + ' | ' + self.tuesday.name + ' | ' + self.wednesday.name \
               + ' | ' + self.thursday.name + ' | ' + self.friday.name + ' | ' + self.saturday.name + ' | ' + self.sunday.name


class Employe(models.Model):
    order = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=100)
    cod_emp = models.PositiveIntegerField()
    last_rol = models.ForeignKey(Matrix, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    valid_weeks = models.PositiveIntegerField(default=4)
    rol_end = models.DateField()

    class Meta:
        verbose_name_plural = 'Empleados'
        verbose_name = 'Empleado'

    def __str__(self):
        return self.name

class EmployeRol(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    rol = models.ForeignKey(Matrix, on_delete=models.CASCADE)
    dates = ArrayField(models.DateField())

    class Meta:
        verbose_name_plural = 'Horario Empleados'
        verbose_name= 'Entrada'

    def __str__(self):
        return self.employe.name