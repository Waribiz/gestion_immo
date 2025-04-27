from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_client = models.BooleanField(default=True)  # Par défaut c'est un client
    is_admin = models.BooleanField(default=False)  # L'admin sera défini manuellement
