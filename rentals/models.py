from django.db import models
from properties.models import Property
from users.models import User
from django.conf import settings


class Contrat(models.Model):
    bien = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='contrats')
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contrats')
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return f"{self.client.username} loue {self.bien} du {self.date_debut} au {self.date_fin}"
 