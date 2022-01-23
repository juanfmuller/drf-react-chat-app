from django.db import models
from django.db.models.fields import related

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.

class Message(models.Model):
  date_time = models.DateTimeField(auto_now_add=True)
  from_user = models.ForeignKey('auth.User', related_name='messages', on_delete=models.CASCADE)
  to_user = models.CharField(max_length=191, blank=False, default=from_user)
  body = models.TextField(blank=False)

  class Meta:
    ordering = ['date_time']

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
  if created:
    Token.objects.create(user=instance)
