from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    fechaNac = models.DateField() 
    edad=models.IntegerField()
    parentesco = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)

   
    

   



