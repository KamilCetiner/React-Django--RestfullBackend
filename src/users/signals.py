from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response


@receiver(post_save, sender=User)

def create_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
    
    return Response(status= status.HTTP_400_BAD_REQUEST)