import django_filters
from .models import Item, ItemHistory



class ItemsFilters(django_filters.FilterSet):
    status = django_filters.NumberFilter(name="status", label='Estado', lookup_expr=['gt', 'lt'])

    class Meta:
        model = Item
        fields = ['serial', 'type', 'system', 'name', 'location', 'status']


class HistoryFilters(django_filters.FilterSet):
    # contains_item = django_filters.BaseInFilter(name="items", lookup_expr='in')

    class Meta:
        model = ItemHistory
        fields = ['item', ]
