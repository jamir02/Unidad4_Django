from django.db import models

# Create your models here.
class usuario(models.Model):

    DNI = models.CharField(max_length=20, default='')
    codigo_usuario = models.CharField(max_length=64, default='')
    clave = models.CharField(max_length=64, default='')

class registro(models.Model):

    nombres= models.CharField(max_length=100, default='')
    apellidos= models.CharField(max_length=100, default='')
    dni= models.CharField(max_length=20, default='')
    usuarios= models.CharField(max_length=150, default='')
    contraseña= models.CharField(max_length=150, default='') 
    fotoperfil= models.CharField(max_length=500, default='') 
    urlgithub= models.CharField(max_length=500, default='') 
    
class proyectos(models.Model):

    dni_1 = models.CharField(max_length=20, default='')
    foto_proy= models.CharField(max_length=500, default='') 
    titulo_proy= models.CharField(max_length=200, default='')  #Recibo la fecha de la creacion de la nueva tarea
    descrip_proy= models.CharField(max_length=500, default='')  #Recibo la fecha de entrega de la nueva tarea
    