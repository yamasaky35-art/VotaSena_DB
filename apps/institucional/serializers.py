from rest_framework import serializers

from .models import BienestarAprendiz, CentroFormacion, Sede


class CentroFormacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroFormacion
        fields = '__all__'


class BienestarAprendizSerializer(serializers.ModelSerializer):
    class Meta:
        model = BienestarAprendiz
        fields = '__all__'


class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'
