from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Carrera(models.Model):
    nombre    = models.CharField(blank=False, null=True, unique=True, max_length=8, verbose_name='Nombre')
    duracion  = models.IntegerField(blank=False, null=True, unique=True, verbose_name='Duracion')

    def __str__(self):
        return '{}'.format(self.nombre)

class Usuario(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    carrera     = models.ForeignKey(Carrera, on_delete=models.SET_NULL, blank=False, null=True, unique=False, max_length=8)
    email       = models.EmailField(max_length=40, unique= True,verbose_name='email')
    imagen      = models.ImageField(upload_to="perfil/", height_field=None, width_field=None)
