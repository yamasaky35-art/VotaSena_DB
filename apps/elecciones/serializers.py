from rest_framework import serializers

from .models import Acta, ComiteElectora, Eleccion, Lista, Voto


class EleccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eleccion
        fields = '__all__'


class ActaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acta
        fields = '__all__'


class ComiteElectoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComiteElectora
        fields = '__all__'


class VotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voto
        fields = '__all__'


class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = '__all__'
