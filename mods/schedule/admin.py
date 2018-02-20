from django.contrib import admin
from .models import Rol, Matrix, Employe, EmployeRol
# Register your models here.

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    pass

@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    pass

@admin.register(EmployeRol)
class EmployeRolAdmin(admin.ModelAdmin):
    pass

@admin.register(Matrix)
class MatrixAdmin(admin.ModelAdmin):
    list_display = ('index', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'tasks',  'total_hours', 'worked_hours', 'extras')
    list_display_links = ('index', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    ordering = ['index']