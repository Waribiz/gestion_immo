from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name= models.CharField(max_length=50, default=None)
    is_client = models.BooleanField(default=True)  # Par défaut c'est un client
    is_admin = models.BooleanField(default=False)  # L'admin sera défini manuellement
