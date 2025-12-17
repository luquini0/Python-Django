from django.db import models

# Create your models here.
class Perro(models.Model):
    raza = models.CharField(max_length=30)
    tamaño = models.CharField(max_length=30)
    
    def __str__(self):
        return f'Perro ({self.id}): {self.raza} - {self.tamaño}'