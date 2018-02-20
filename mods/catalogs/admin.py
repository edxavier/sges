from django.contrib import admin
from .models import Item, ItemHistory, ItemStatus, ItemType, System, Service,\
    ServiceType, ServiceCategory, Location
# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'location', 'system','status')
    ordering = ['type__name']

@admin.register(ItemHistory)
class ItemHistoryAdmin(admin.ModelAdmin):
    list_display = ('item', 'location', 'status', 'created_by', 'created_at')
    ordering = ['-created_at']


@admin.register(ItemStatus)
class ItemStatusAdmin(admin.ModelAdmin):
    pass

@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    pass

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'type', 'owner')
    ordering = ['category__name']


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass