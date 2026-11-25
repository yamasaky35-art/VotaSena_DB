from django.db import models

from django.db import models


class ProgramaFormacion(models.Model):
    codigo_programa = models.CharField(max_length=10, primary_key=True)
    nombre_programa = models.CharField(max_length=100)
    nivel_formacion = models.CharField(max_length=20)

    def __str__(self):
        return f'Nombre del programa {self.nombre_programa} con un nivel de formacion {self.nivel_formacion}'


class ProgramaSede(models.Model):
    codigo_programa = models.ForeignKey(ProgramaFormacion, on_delete=models.CASCADE, db_column='codigo_programa')
    codigo_sede = models.ForeignKey('institucional.Sede', on_delete=models.CASCADE, db_column='codigo_sede')

    class Meta:
        unique_together = (('codigo_programa', 'codigo_sede'),)

    def __str__(self):
        return f'Programa {self.codigo_programa} sede {self.codigo_sede}'


class Jornada(models.Model):
    id_jornada = models.CharField(max_length=10, primary_key=True)
    nombre_jornada = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'La jornada es {self.nombre_jornada}'


class Rol(models.Model):
    id_rol = models.CharField(max_length=10, primary_key=True)
    nombre_rol = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'Su rol es {self.nombre_rol}'


class Ficha(models.Model):
    numero_ficha = models.CharField(max_length=10, primary_key=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    id_jornada = models.ForeignKey(Jornada, on_delete=models.CASCADE, db_column='id_jornada')
    codigo_programa = models.ForeignKey(ProgramaFormacion, on_delete=models.CASCADE, db_column='codigo_programa')
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, db_column='id_rol')

    def __str__(self):
        return f'Su numero de ficha es {self.numero_ficha}'