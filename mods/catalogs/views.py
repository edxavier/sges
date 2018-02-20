from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import *
from .filters import HistoryFilters

# Create your views here.


class FormsViewSet(viewsets.ViewSet):
    def list(self, request):
        itemType_queryset = ItemType.objects.all().order_by('name')
        itemType_serializer = ItemTypeSerializer(itemType_queryset, many=True)

        system_queryset = System.objects.all().order_by('name')
        system_serializer = SystemSerializer(system_queryset, many=True)

        location_queryset = Location.objects.all().order_by('name')
        location_serializer = LocationSerializer(location_queryset, many=True)

        status_queryset = ItemStatus.objects.all().order_by('name')
        status_serializer = ItemStatusSerializer(status_queryset, many=True)

        return Response({
            'types': itemType_serializer.data,
            'systems': system_serializer.data,
            'locations': location_serializer.data,
            'statuses': status_serializer.data
        })


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(active=True).order_by('name')
    serializer_class = ItemSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.filter(active=True).order_by('name')
    serializer_class = ServiceSerializer


class ItemHistoryViewSet(viewsets.ModelViewSet):
    queryset = ItemHistory.objects.filter(active=True).order_by('-created_at')
    serializer_class = ItemHistorySerializer
    filter_class = HistoryFilters

    def create(self, request, *args, **kwargs):
        try:
            serial = ItemHistorySerializer(data=request.data)
            item = Item.objects.get(id=request.data['item'])
            stat = ItemStatus.objects.get(id=request.data['status'])
            location = Location.objects.get(id=request.data['location'])
            item.status = stat
            item.location = location
            item.version = request.data['version']
            item.save()
            if serial.is_valid():
                serial.save()
                return Response(serial.data)
            else:
                return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
