from django.db import models
from properties.models import Property
from users.models import User

class Contrat(models.Model):
    bien = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='contrats')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contrats', limit_choices_to={'role': 'client'})
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return f"Contrat #{self.id} pour {self.bien}"
