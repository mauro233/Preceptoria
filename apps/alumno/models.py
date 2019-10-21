from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Alumno(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, blank=True, help_text='Ingrese su nombre.')
    apellido = models.CharField(max_length=50, blank=True, help_text='Ingrese su apellido.')
    correo = models.EmailField(blank=True, help_text='Ingrese su correo electrónico.')
    
    class Meta:
    	verbose_name='Alumno'
    	verbose_name_plural= 'Alumnos'

    # Python 3
    def __str__(self): 
        return self.usuario.username

@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Alumno.objects.create(usuario=instance)
# post_save lo que hace es crear el perfil después que un usuario es registrado.
@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.alumno.save()
  