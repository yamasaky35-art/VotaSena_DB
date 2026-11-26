from rest_framework import serializers

from .models import Ficha, Jornada, ProgramaFormacion, ProgramaSede, Rol


class ProgramaFormacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramaFormacion
        fields = '__all__'


class ProgramaSedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramaSede
        fields = '__all__'


class JornadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jornada
        fields = '__all__'


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'


class FichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ficha
        fields = '__all__'
