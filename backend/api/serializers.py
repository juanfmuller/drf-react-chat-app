from decimal import Context
from django.db.models import fields
from rest_framework import serializers
from api.models import Message
from django.contrib.auth.models import User
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

class MessageSerializer(serializers.HyperlinkedModelSerializer):
  from_user = serializers.ReadOnlyField(source='from_user.username')

  class Meta:
    model = Message
    fields = ['url', 'id', 'from_user', 'to_user', 'body']

class UserSerializer(serializers.HyperlinkedModelSerializer):

  messages = serializers.HyperlinkedRelatedField(many=True, view_name='message-detail', read_only=True)

  class Meta:
    model = User
    fields = ['url', 'id', 'username', 'password', 'messages']

  def create(self, validated_data):
    user = User.objects.create(
        username=validated_data['username']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user