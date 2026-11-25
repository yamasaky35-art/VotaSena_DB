from django.db import models

from django.db import models


class Departamento(models.Model):
    id_departamento = models.CharField(max_length=2, primary_key=True)
    nombre_departamento = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return f'El id del departamento es {self.id_departamento} y el nombre es {self.nombre_departamento}'


class Municipio(models.Model):
    id_municipio = models.CharField(max_length=5, primary_key=True)
    nombre_municipio = models.CharField(max_length=30)
    id_departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, db_column='id_departamento')

    class Meta:
        unique_together = (('nombre_municipio', 'id_departamento'),)

    def __str__(self):
        return f'Id del municipio {self.id_municipio} nombre del municipio {self.nombre_municipio}'