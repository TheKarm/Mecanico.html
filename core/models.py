from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Genero(models.Model):
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

class TipoMecanico(models.Model):
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

class Mecanico(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField(default=0)
    direccion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=20)
    habilitado = models.BooleanField(default=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoMecanico, on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    imagen = CloudinaryField('imagen')

    def __str__(self):
        return self.rut
    

class Cliente(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)  # Cambiado a primary_key=True
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    contrase = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)

    def str(self):
        return self.rut

class Producto(models.Model):
    idP = models.AutoField(primary_key=True)  # AutoField para generar automáticamente el ID
    nombreP = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    valor = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    numero = models.IntegerField()

    def str(self):
        return self.nombreP

class Venta(models.Model):
    idV = models.CharField(max_length=12, primary_key=True)
    nombreV = models.CharField(max_length=40)
    fechaCompra = models.DateTimeField()  # No usar auto_now_add=True
    total = models.IntegerField()
    descripcion = models.CharField(max_length=40)

    def str(self):
        return self.idV

class DetalleVenta(models.Model):
    idDet = models.CharField(max_length=12, primary_key=True)
    nombreDet = models.CharField(max_length=40)
    fechaCompra = models.DateTimeField()  # No usar auto_now_add=True
    fechaEntrega = models.DateTimeField()  # No usar auto_now_add=True
    totalD = models.IntegerField()
    descripcionD = models.CharField(max_length=40)

    def str(self):
        return self.idDet

class Carrito(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField(default=1)

    def str(self):
        return self.nombre