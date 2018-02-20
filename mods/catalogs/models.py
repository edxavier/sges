from django.db import models
from shared.Helpers import TimeStamp
from mods.users.models import User
# Create your models here.
# Create your models here.


class ServiceCategory(TimeStamp):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, verbose_name='Descripcion')

    class Meta:
        verbose_name_plural = 'Categorias de servicio'
        verbose_name = 'Categoria de servicio'

    def __str__(self):
        return self.name

class ServiceType(TimeStamp):
    """
        -Internos, Externos
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, verbose_name='Descripcion')

    class Meta:
        verbose_name_plural = 'Tipos de servicio'
        verbose_name = 'Tipo de servicio'

    def __str__(self):
        return self.name

class Service(TimeStamp):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(ServiceCategory, verbose_name="Categoria del servicio", on_delete=models.CASCADE)
    type = models.ForeignKey(ServiceType, verbose_name="Tipo de servicio", on_delete=models.CASCADE)
    owner = models.CharField(blank=True, max_length=100, verbose_name='Propietario del servicio')
    description = models.TextField(blank=True, verbose_name='Descripcion', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Servicios'
        verbose_name = 'Servicio'



class ItemType(TimeStamp):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Tipos de Elementos'
        verbose_name = 'Tipo de Elemento'

    def __str__(self):
        return self.name


class Location(TimeStamp):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Ubicaciones'
        verbose_name = 'Ubicacion'

    def __str__(self):
        return self.name


class ItemStatus(TimeStamp):
    # Operativo - Degradado - Fallo - Reserva - De baja
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Estados Operativos'
        verbose_name = 'Estado'

    def __str__(self):
        return self.name


class System(TimeStamp):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Sistemas'
        verbose_name = 'Sistema'

    def __str__(self):
        return self.name


class Item(TimeStamp):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='S/D')
    type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=100, blank=True, default='----')
    serial = models.CharField(max_length=100, blank=True, default='----')
    version = models.CharField(max_length=100, blank=True, default='----')
    inventory = models.CharField(max_length=100, blank=True, default='----')
    location = models.ForeignKey(Location, default=None, on_delete=models.CASCADE)
    status = models.ForeignKey(ItemStatus, null=True, blank=True, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'Elementos'
        verbose_name = 'Elemento'

    def __str__(self):
        return self.name


class ItemHistory(TimeStamp):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    history_description = models.TextField()
    version = models.CharField(max_length=100, null=True, blank=True)
    location = models.ForeignKey(Location, default=None, on_delete=models.CASCADE)
    status = models.ForeignKey(ItemStatus, null=True, blank=True, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name_plural = 'Historial de elementos'
        verbose_name = 'Historial de elemento'

    def __str__(self):
        return self.item.name