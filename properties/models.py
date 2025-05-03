from django.db import models
from users.models import User

class Property(models.Model):
    TYPE_CHOICES = (
        ('appartement', 'Appartement'),
        ('maison', 'Maison'),
        ('bureau', 'Bureau'),
        ('terrain', 'Terrain'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)
    property_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
