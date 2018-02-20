from django.db import models
from shared.Helpers import TimeStamp
from mods.catalogs.models import Service, Item
from mods.users.models import User
# Create your models here.


class ChangeStatus(TimeStamp):
    # Planificado - Pendiente - En proceso - Retrazado - Cancelado - Terminado
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Estados de cambio'
        verbose_name = 'Estado de cambio'

class TaskType(TimeStamp):
    # Mantenimiento precentivo - Trabajos Correctivos - Trabajos no planificados
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Tipos de tareas'
        verbose_name = 'Tipo de tarea'


class Change(TimeStamp):
    title = models.CharField(max_length=100)
    request_by = models.CharField(max_length=200)
    executed_by = models.CharField(max_length=200)
    justification = models.TextField()
    planned_start = models.DateField()
    planned_completion = models.DateField()
    started_on = models.DateField(blank=True, null=True)
    finished_on = models.DateField(blank=True, null=True)
    change_status = models.ForeignKey(ChangeStatus, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='change_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='change_updated_by')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Cambios'
        verbose_name = 'Cambio'


class ChangeEntry(TimeStamp):
    change = models.ForeignKey(Change, on_delete=models.CASCADE, related_name='change_entries')
    changes = models.TextField()
    affected_services = models.ManyToManyField(Service, blank=True)
    affected_items = models.ManyToManyField(Item, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.change.title

    class Meta:
        verbose_name_plural = 'Entradas de cambios'
        verbose_name = 'Entrada de cambio'


class Task(TimeStamp):
    type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    description = models.TextField(default='', blank=True)
    planned_start = models.DateField()
    planned_completion = models.DateField()
    started_on = models.DateField(blank=True, null=True)
    finished_on = models.DateField(blank=True, null=True)
    task_status = models.ForeignKey(ChangeStatus, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='task_updated_by')

    def __str__(self):
        return self.type.name

    class Meta:
        verbose_name_plural = 'Trabajos'
        verbose_name = 'Trabajo'

class TaskEntry(TimeStamp):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_entries' )
    description = models.TextField()
    affected_services = models.ManyToManyField(Service, blank=True)
    affected_items = models.ManyToManyField(Item, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task.type.name

    class Meta:
        verbose_name_plural = 'Entradas de trabajos'
        verbose_name = 'Entrada de trabajo'



class Severity(TimeStamp):
    # Planificado - Pendiente - En proceso - Retrazado - Cancelado - Terminado
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, default='S/D')
    class Meta:
        verbose_name_plural = 'Serveridad de incidentes'
        verbose_name = 'Serveridad'
    def __str__(self):
        return self.name

class IncidentCategory(TimeStamp):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = 'Categorias de incidentes'
        verbose_name = 'Categoria de incidente'
    def __str__(self):
        return self.name

class IncidentStatus(TimeStamp):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = 'Estados de incidentes'
        verbose_name = 'Estado de incidente'
    def __str__(self):
        return self.name


class IncidentSource(TimeStamp):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = 'Origen de incidentes'
        verbose_name = 'Origen de incidente'
    def __str__(self):
        return self.name


class Incident(TimeStamp):
    title = models.CharField(max_length=150)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incident_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='incident_updated_by')
    notified_by = models.CharField(max_length=100)
    incident_description = models.TextField()
    severity = models.ForeignKey(Severity, on_delete=models.CASCADE)
    category = models.ForeignKey(IncidentCategory, on_delete=models.CASCADE)
    source = models.ForeignKey(IncidentSource, on_delete=models.CASCADE)
    status = models.ForeignKey(IncidentStatus, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Incidentes'
        verbose_name = 'Incidente'

    def __str__(self):
        return self.title

class IncidentEntry(TimeStamp):
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE, related_name='incident_entries')
    description = models.TextField()
    affected_services = models.ManyToManyField(Service, blank=True, )
    affected_items = models.ManyToManyField(Item, blank=True,)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Entradas de incidentes'
        verbose_name = 'Entrada de incidente'
        ordering = ['-created_at']

    def __str__(self):
        return self.incident.title


class KnownErrors(TimeStamp):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kerror_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='kerror_updated_by')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Errores Conocidos'
        verbose_name = 'Error conocido'