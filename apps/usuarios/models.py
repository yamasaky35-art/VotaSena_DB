from django.db import models

class Persona(models.Model):
    num_documento = models.CharField(max_length=10, primary_key=True)
    tipo_documento = models.CharField(max_length=2)
    nombre_p = models.CharField(max_length=80)
    nombre_s = models.CharField(max_length=80, blank=True, null=True)
    apellido_p = models.CharField(max_length=80)
    apellido_s = models.CharField(max_length=80, blank=True, null=True)
    correo_institucional = models.EmailField(max_length=200, unique=True)
    correo_personal = models.EmailField(max_length=200, unique=True)
    ciudad_residencia = models.CharField(max_length=60)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=150)
    foto = models.TextField(blank=True, null=True)
    codigo_sede = models.ForeignKey('institucional.Sede', on_delete=models.CASCADE, db_column='codigo_sede')
    id_rol = models.ForeignKey('academico.Rol', on_delete=models.CASCADE, db_column='id_rol')
    id_bienestar = models.ForeignKey('institucional.BienestarAprendiz', on_delete=models.CASCADE, db_column='id_bienestar')
    id_comite = models.ForeignKey('elecciones.ComiteElectora', on_delete=models.CASCADE, db_column='id_comite')
    uuid_lista = models.ForeignKey('elecciones.Lista', on_delete=models.SET_NULL, null=True, blank=True, db_column='uuid')

    def __str__(self):
        return f'Su tipo de identificacion es {self.tipo_documento} y su numero de documento {self.num_documento} identificado {self.nombre_p} {self.apellido_p}'


class Aprendiz(models.Model):
    num_documento = models.OneToOneField(Persona, on_delete=models.CASCADE, primary_key=True, db_column='num_documento')
    estado = models.BooleanField(default=True)
    numero_ficha = models.ForeignKey('academico.Ficha', on_delete=models.CASCADE, db_column='numero_ficha')
    codigo_programa = models.ForeignKey('academico.ProgramaFormacion', on_delete=models.CASCADE, db_column='codigo_programa')
    id_voto = models.OneToOneField('elecciones.Voto', on_delete=models.SET_NULL, null=True, blank=True, db_column='id_voto')

    def __str__(self):
        return f'Su numero de documento es {self.num_documento} y su estado es {self.estado}'


class CandidatoPostulado(models.Model):
    num_documento = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='num_documento')
    tipo_postulacion = models.CharField(max_length=20)
    propuestas = models.TextField()

    class Meta:
        unique_together = (('num_documento', 'tipo_postulacion'),)

    def __str__(self):
        return f'Su numero de documento es {self.num_documento} con una propuesta.'