from django.contrib import admin
# Register your models here.
from django.contrib.auth.admin import UserAdmin

from mods.users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        ('Informacion de Acceso', {'fields': ('username', 'password')}),
        ('Informacion Personal', {'fields': ('first_name', 'last_name', 'employee_code', 'email',)}),
        ('Permisos', {'fields': (('is_staff', 'is_superuser', 'is_active'), 'groups', 'user_permissions')}),
    )