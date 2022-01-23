from django.contrib.auth.models import User
from rest_framework import (generics, permissions, renderers, serializers,
                            status)
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from api.models import Message
from api.permissions import IsOwnerOrReadOnly
from api.serializers import MessageSerializer, UserSerializer

# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
  return Response({
      'users': reverse('user-list', request=request, format=format),
      'messages': reverse('message-list', request=request, format=format),
  })


class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  
  def post(self, request, format=None):
    serializer = UserSerializer(data=request.data, context={'request': request})
    res_data = {}
    if serializer.is_valid():
        account = serializer.save()
        res_data['response'] = "Successfully registered a new user"
        res_data['username'] = account.username
        token = Token.objects.get(user=account).key
        res_data['token'] = token
        return Response(res_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class MessageList(generics.ListCreateAPIView):
  queryset = Message.objects.all()
  serializer_class = MessageSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(from_user=self.request.user)


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Message.objects.all()
  serializer_class = MessageSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                    IsOwnerOrReadOnly]
