from django.db import models

# Create your models here.

class formularioContacto(models.Model):
    nombreCliente = models.CharField(primary_key=True, max_length=255)
    correoGmail = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    marca = models.CharField(max_length=30, default="")
    modeloAuto = models.CharField(max_length=50, default="")
    tipoServicio = models.CharField(max_length=25, default="")
    descripcion = models.CharField(max_length=50, default="")

    def __str__(self):
        return str(self.nombreCliente)+" "+str(self.correoGmail)+" "+str(self.marca)+" "+str(self.modeloAuto)+" "+str(self.tipoServicio)+" "+str(self.descripcion)   

class Atencion(models.Model):
     trabajo = models.CharField(primary_key=True, max_length=255)
     diagnostico = models.CharField(max_length=50)
     fecha = models.DateField(max_length=50)
     modeloAuto = models.CharField(max_length=50)
     imagenAuto = models.CharField(max_length=10)
     categoria = models.CharField(max_length=50, blank=True)
     materiales = models.CharField(max_length=500, blank=True)
     nombreMecanico = models.CharField(max_length=45)
     cliente = models.ForeignKey(formularioContacto, on_delete=models.CASCADE)
     rutCliente = models.CharField(max_length=45)
     costo = models.CharField(max_length=40)
     garantia = models.CharField(max_length=30)
     verify = models.CharField(max_length=1, blank=True)

     def __str__(self):
        return str(self.trabajo)+" "+str(self.diagnostico)+" "+str(self.fecha)+" "+str(self.modeloAuto)+" "+str(self.imagenAuto)+" "+str(self.categoria)+" "+str(self.materiales)+" "+str(self.nombreMecanico)+" "+str(self.cliente.nombreCliente)+" "+str(self.rutCliente)+" "+str(self.costo)+" "+str(self.garantia)+" "+str(self.verify)



class formularioRes(models.Model):
     trabajos = models.CharField(primary_key=True, max_length=255)
     estado = models.CharField(max_length=50)
     tipoAtencion = models.CharField(max_length=50)
     diasHabiles = models.CharField(max_length=30)
     justificacion = models.CharField(max_length=300)

     def __str__(self):
        return str(self.trabajos)+" "+str(self.estado)+" "+str(self.tipoAtencion)+" "+str(self.diasHabiles)+" "+(self.justificacion)

