<<<<<<< HEAD
from django.db import models

# Create your models here.
class Perro(models.Model):
    raza = models.CharField(max_length=30)
    tamaño = models.CharField(max_length=30)
    
    def __str__(self):
=======
from django.db import models

# Create your models here.
class Perro(models.Model):
    raza = models.CharField(max_length=30)
    tamaño = models.CharField(max_length=30)
    
    def __str__(self):
>>>>>>> dd686a4e1f4202362c07ebce170f5dcb86ca1bbc
        return f'Perro ({self.id}): {self.raza} - {self.tamaño}'