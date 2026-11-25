from django.db import models

from django.db import models


class CentroFormacion(models.Model):
    nit = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=150, unique=True)
    correo = models.EmailField(max_length=200, unique=True)
    id_municipio = models.ForeignKey('ubicacion.Municipio', on_delete=models.CASCADE, db_column='id_municipio')

    def __str__(self):
        return f'Nombre del centro de formacion {self.nombre}'


class BienestarAprendiz(models.Model):
    id_bienestar = models.CharField(max_length=10, primary_key=True)
    area_encargada = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return f'El area encargada del bienestar al aprendiz es {self.area_encargada}'


class Sede(models.Model):
    codigo_sede = models.CharField(max_length=10, primary_key=True)
    nombre_sede = models.CharField(max_length=100)
    direccion_sede = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20)
    nit = models.ForeignKey(CentroFormacion, on_delete=models.CASCADE, db_column='nit')
    id_bienestar = models.ForeignKey(BienestarAprendiz, on_delete=models.CASCADE, db_column='id_bienestar')

    def __str__(self):
        return f'La sede es {self.nombre_sede} ubicado en {self.direccion_sede} y su numero de contacto {self.telefono}'