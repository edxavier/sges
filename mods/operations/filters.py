from django_filters import rest_framework as filters
from .models import Incident, Task, Change



class IncidentFilters(filters.FilterSet):
    incident_description = filters.CharFilter(name="incident_description", lookup_expr='icontains')
    category__is = filters.BaseInFilter(name="category", lookup_expr='in')# category__is=1,2,3
    created = filters.DateFromToRangeFilter(name='created_at')

    class Meta:
        model = Incident
        fields = ['incident_description', 'status', 'category__is', 'created', 'severity', 'category', 'source']

class TaskFilters(filters.FilterSet):
    type__is = filters.BaseInFilter(name="type", lookup_expr='in')# category__is=1,2,3
    created = filters.DateFromToRangeFilter(name='created_at')

    class Meta:
        model = Task
        fields = ['type__is', 'created']


class ChangeFilters(filters.FilterSet):
    type__is = filters.BaseInFilter(name="type", lookup_expr='in')# category__is=1,2,3
    created = filters.DateFromToRangeFilter(name='created_at')

    class Meta:
        model = Change
        fields = '__all__'
