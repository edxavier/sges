from django.contrib.auth.models import Group, Permission, ContentType
from rest_framework import viewsets
from .models import User
from .serializers import UserListSerializer, UserDetailSerializer
    #GroupSerializer, PermissionSerializer, ContentTypeSerializer

# Create your views here.

def jwt_response_payload_handler(token, user=None, request=None):
    """Funcion para rescribir la respuesta de JWT al solicitar el token"""
    return {
        'token': token,
        'user': UserDetailSerializer(user, context={'request': request}).data
    }


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserListSerializer


"""
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ContentTypeViewSet(viewsets.ModelViewSet):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
"""