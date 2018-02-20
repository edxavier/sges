from django.contrib import admin
from .models import Incident, Severity, IncidentCategory, IncidentEntry, IncidentStatus, \
    KnownErrors, Task, TaskEntry, TaskType, Change, ChangeStatus, ChangeEntry, IncidentSource
# Register your models here.

@admin.register(IncidentSource)
class IncidentSourceAdmin(admin.ModelAdmin):
    pass

@admin.register(ChangeEntry)
class ChangeEntryAdmin(admin.ModelAdmin):
    pass

@admin.register(ChangeStatus)
class ChangeStatusAdmin(admin.ModelAdmin):
    pass

@admin.register(Change)
class ChangeAdmin(admin.ModelAdmin):
    pass

@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(TaskEntry)
class TaskEntryAdmin(admin.ModelAdmin):
    pass

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    pass


@admin.register(IncidentEntry)
class IncidentEntryAdmin(admin.ModelAdmin):
    pass

@admin.register(Severity)
class SeverityAdmin(admin.ModelAdmin):
    pass


@admin.register(IncidentCategory)
class IncidentCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(IncidentStatus)
class IncidentStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(KnownErrors)
class KnownErrorsAdmin(admin.ModelAdmin):
    pass