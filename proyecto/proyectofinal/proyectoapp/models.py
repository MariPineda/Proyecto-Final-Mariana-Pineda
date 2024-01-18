from django.db import models

from django.contrib.auth.models import User

class Socios(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    socio = models.IntegerField()
    activo = models.BooleanField()

    class Meta:
        verbose_name_plural = "Socios"
        ordering = ["apellido"]

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email} {self.socio} {self.activo}"

class Libros(models.Model):
    titulo = models.CharField(max_length=40)
    tipo = models.CharField(max_length=60)
    edadRecomendada = models.IntegerField()

    class Meta:
        verbose_name_plural = "Libros"

    def __str__(self):
        return f"{self.titulo}"
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.image}" 

