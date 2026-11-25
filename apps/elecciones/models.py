from django.db import models

class Eleccion(models.Model):
    id_eleccion = models.CharField(max_length=10, primary_key=True)
    tipo_eleccion = models.CharField(max_length=50)
    fecha_inicio_eleccion = models.DateField()
    fecha_fin_eleccion = models.DateField()
    estado = models.BooleanField(default=True)
    descripcion = models.TextField()
    id_bienestar = models.ForeignKey('institucional.BienestarAprendiz', on_delete=models.CASCADE, db_column='id_bienestar')
    id_rol = models.ForeignKey('academico.Rol', on_delete=models.CASCADE, db_column='id_rol')

    def __str__(self):
        return f'El tipo de eleccion es {self.tipo_eleccion} teniendo inicio el día {self.fecha_inicio_eleccion}'


class Acta(models.Model):
    id_acta = models.CharField(max_length=20, primary_key=True)
    descripcion_acta = models.TextField()
    id_eleccion = models.ForeignKey(Eleccion, on_delete=models.CASCADE, db_column='id_eleccion')

    def __str__(self):
        return f'El id del acta es {self.id_acta} la descripcion es {self.descripcion_acta}'


class ComiteElectora(models.Model):
    id_comite = models.CharField(max_length=10, primary_key=True)
    estado_comite = models.BooleanField(default=True)
    numero_miembros = models.IntegerField()
    id_acta = models.ForeignKey(Acta, on_delete=models.CASCADE, db_column='id_acta')

    def __str__(self):
        return f'Comite {self.id_comite} con {self.numero_miembros} miembros'


class Voto(models.Model):
    id_voto = models.CharField(max_length=20, primary_key=True)
    fecha_voto = models.DateField()
    id_eleccion = models.ForeignKey(Eleccion, on_delete=models.CASCADE, db_column='id_eleccion')

    def __str__(self):
        return f'Su identificador del voto es {self.id_voto} y la fecha del dia {self.fecha_voto}'


class TipoListaChoices(models.TextChoices):
    PRINCIPAL = 'Principal', 'Principal'
    ALTERNATIVA = 'Alternativa', 'Alternativa'


class Lista(models.Model):
    uuid = models.CharField(max_length=50, primary_key=True)
    tipo_lista = models.CharField(max_length=50, choices=TipoListaChoices.choices, default=TipoListaChoices.PRINCIPAL)
    id_clave = models.CharField(max_length=50, unique=True)
    valor = models.CharField(max_length=100)
    descripcion = models.TextField()

    class Meta:
        db_table = 'lista'

    def __str__(self):
        return f'{self.valor} ({self.tipo_lista})'