from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import *
from .filters import IncidentFilters, TaskFilters, ChangeFilters
from .paginators import OperationsPaginator
from datetime import datetime
from django.db.models import F
from django.db.models import Count, Sum
from django.db.models.functions import Cast
from django.db.models import FloatField
# Create your views here.

class IncidentResumeViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.filter(active=True).order_by('-created_at')
    serializer_class = IncidentSerializer
    filter_class = IncidentFilters

    def list(self, request):
        total =  self.filter_queryset(Incident.objects.filter(active=True).order_by('-created_at'))
        print(total.count() )

        status = self.filter_queryset(Incident.objects
                                      .annotate(name=F('status__name'))# Renombrar el campo
                                      .values('name').filter(active=True).filter(active=True)
                                      .annotate(y=Count('status')).order_by('-y'))
        source = self.filter_queryset(Incident.objects.values('source__name').filter(active=True)
                                               .annotate(total=Count('source')).order_by('-total'))
        severity = self.filter_queryset(Incident.objects.values('severity__name').filter(active=True)
                                               .annotate(total=Count('severity')).order_by('-total'))

        category = self.filter_queryset(Incident.objects.values('category__name').filter(active=True)
                                        .annotate(perc=Cast(Count('category') * 100.0 / total.count(), FloatField()))
                                        .annotate(total=Count('category')).order_by('-total'))

        services = self.filter_queryset(Incident.objects
                                 .annotate(name=F('incident_entries__affected_services__name'))  # Renombrar el campo
                                 .values('name')
                                 .filter(active=True)
                                 .annotate(total=Count('name')).order_by('-total').filter(total__gt=0))

        services_ = self.filter_queryset(Incident.objects
                                 .annotate(name=F('incident_entries__affected_services__name'))  # Renombrar el campo
                                 .values('name')
                                 .filter(active=True, name__isnull=False))
        print(services_.count())

        items = self.filter_queryset(Incident.objects
                                 .annotate(name=F('incident_entries__affected_items__name'))  # Renombrar el campo
                                 .values('name')
                                 .filter(active=True)
                                 .annotate(total=Count('name')).order_by('-total').filter(total__gt=0))

        # services = IncidentEntry.objects.values('affected_services__name').filter(active=True, ).annotate(total=Count('affected_services')).order_by('-total')
        # print(services)

        return Response({
            'status': status,
            'severity': severity,
            'sources': source,
            'category': category,
            'services': services,
            'items': items
        })


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.filter(active=True).order_by('status', '-created_at')
    serializer_class = IncidentSerializer
    filter_class = IncidentFilters
    pagination_class = OperationsPaginator

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = IncidentSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkaroundViewSet(viewsets.ModelViewSet):
    queryset = KnownErrors.objects.filter(active=True).order_by('-created_at')
    serializer_class = WorkaroundSerializer
    pagination_class = OperationsPaginator
    filter_fields = ('id',)

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = WorkaroundSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskViewSet(viewsets.ModelViewSet):
    #queryset = Task.objects.filter(active=True).order_by('-created_at')
    serializer_class = TaskSerializer
    pagination_class = OperationsPaginator
    filter_class = TaskFilters

    def get_queryset(self):
        queryset = Task.objects.filter(active=True).order_by('task_status', '-created_at')
        # Actualizar las tareas planificadas per pendiente y en proceso pero atrazadas
        Task.objects.filter(active=True, planned_start__lt=datetime.now().date(), task_status=1)\
            .update(task_status=2)
        Task.objects.filter(active=True, planned_completion__lt=datetime.now().date(), task_status=3) \
            .update(task_status=2)
        return queryset

    """def list(self, request, *args, **kwargs):
        tasks = self.filter_queryset(Task.objects.filter(active=True).order_by('-created_at'))
        paginator = OperationsPaginator()
        page = paginator.paginate_queryset(tasks, request)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            paginator.request = self.request
            return paginator.get_paginated_response(serializer.data)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)"""

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = TaskSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangeViewSet(viewsets.ModelViewSet):
    #queryset = Task.objects.filter(active=True).order_by('-created_at')
    serializer_class = ChangeSerializer
    pagination_class = OperationsPaginator
    filter_class = ChangeFilters

    def get_queryset(self):
        queryset = Change.objects.filter(active=True).order_by('change_status', '-created_at')
        # Actualizar las tareas planificadas per pendiente y en proceso pero atrazadas
        Change.objects.filter(active=True, planned_start__lt=datetime.now().date(), change_status=1)\
            .update(change_status=2)
        Change.objects.filter(active=True, planned_completion__lt=datetime.now().date(), change_status=3) \
            .update(change_status=2)
        return queryset

    """def list(self, request, *args, **kwargs):
        tasks = self.filter_queryset(Task.objects.filter(active=True).order_by('-created_at'))
        paginator = OperationsPaginator()
        page = paginator.paginate_queryset(tasks, request)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            paginator.request = self.request
            return paginator.get_paginated_response(serializer.data)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)"""

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = ChangeSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IncidentEntryViewSet(viewsets.ModelViewSet):
    queryset = IncidentEntry.objects.filter(active=True).order_by('-id')
    serializer_class = IncidentEntrySerializer


    def create(self, request, *args, **kwargs):
        try:
            serial = IncidentEntrySerializer(data=request.data)
            incident = Incident.objects.get(id=request.data['incident'])
            incident.status = IncidentStatus.objects.get(id=2)
            incident.save()
            if serial.is_valid():
                serial.save()
                return Response(serial.data)
            else:
                return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)


class TaskEntryViewSet(viewsets.ModelViewSet):
    queryset = TaskEntry.objects.filter(active=True).order_by('-id')
    serializer_class = TaskEntrySerializer

    def create(self, request, *args, **kwargs):
        try:
            serial = TaskEntrySerializer(data=request.data)
            task = Task.objects.get(id=request.data['task'])
            entries = TaskEntry.objects.filter(task=task.id)
            now = datetime.now()
            if entries.count() <= 0:
                task.started_on = now.date()

            if task.planned_completion > now.date():
                task.task_status = ChangeStatus.objects.get(id=3)
            else:
                task.task_status = ChangeStatus.objects.get(id=4)

            task.save()
            if serial.is_valid():
                serial.save()
                return Response({
                                 'started_on': task.started_on,
                                 'status_id': task.task_status.id,
                                 'status_name': task.task_status.name,
                                 'entry': serial.data
                                },
                                status=status.HTTP_200_OK)
                # return Response(serial.data)
            else:
                return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'Error global, no se puedo completar la operacion'}, status=status.HTTP_400_BAD_REQUEST)



class ChangeEntryViewSet(viewsets.ModelViewSet):
    queryset = ChangeEntry.objects.filter(active=True).order_by('-id')
    serializer_class = ChangeEntrySerializer

    def create(self, request, *args, **kwargs):
        try:
            serial = self.get_serializer(data=request.data)
            change = Change.objects.get(id=request.data['change'])
            entries = ChangeEntry.objects.filter(change=change.id)
            now = datetime.now()
            if entries.count() <= 0:
                change.started_on = now.date()

            if change.planned_completion > now.date():
                change.change_status = ChangeStatus.objects.get(id=3)
            else:
                change.change_status = ChangeStatus.objects.get(id=4)

            change.save()
            if serial.is_valid():
                serial.save()
                return Response({
                                 'started_on': change.started_on,
                                 'status_id': change.change_status.id,
                                 'status_name': change.change_status.name,
                                 'entry': serial.data
                                },
                                status=status.HTTP_200_OK)
                # return Response(serial.data)
            else:
                return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'Error global, no se puedo completar la operacion'}, status=status.HTTP_400_BAD_REQUEST)



class FormsViewSet(viewsets.ViewSet):
    def list(self, request):
        status_queryset = IncidentStatus.objects.filter(active=True).order_by('id')
        status_serializer = IncidentStatusSerializer(status_queryset, many=True)

        severity_queryset = Severity.objects.filter(active=True).order_by('id')
        severity_serializer = SeveritySerializer(severity_queryset, many=True)

        categories_queryset = IncidentCategory.objects.filter(active=True).order_by('name')
        categories_serializer = CategorySerializer(categories_queryset, many=True)

        source_queryset = IncidentSource.objects.filter(active=True).order_by('name')
        source_serializer = IncidentSourceSerializer(source_queryset, many=True)

        return Response({
            'categories': categories_serializer.data,
            'severities': severity_serializer.data,
            'statuses': status_serializer.data,
            'sources': source_serializer.data
        })


class TaskFormsViewSet(viewsets.ViewSet):
    def list(self, request):
        status_queryset = ChangeStatus.objects.filter(active=True).order_by('id')
        status_serializer = ChangetStatusSerializer(status_queryset, many=True)

        type_queryset = TaskType.objects.filter(active=True).order_by('id')
        type_serializer = TaskTypeSerializer(type_queryset, many=True)

        return Response({
            'status': status_serializer.data,
            'type': type_serializer.data
        })

