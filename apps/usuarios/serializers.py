from rest_framework import serializers

from .models import Aprendiz, CandidatoPostulado, Persona


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'


class AprendizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aprendiz
        fields = '__all__'


class CandidatoPostuladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidatoPostulado
        fields = '__all__'
