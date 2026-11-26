from django.shortcuts import render
from rest_framework import viewsets

from .models import Acta, ComiteElectora, Eleccion, Lista, Voto
from .serializers import (
    ActaSerializer,
    ComiteElectoraSerializer,
    EleccionSerializer,
    ListaSerializer,
    VotoSerializer,
)


class EleccionViewSet(viewsets.ModelViewSet):
    queryset = Eleccion.objects.all()
    serializer_class = EleccionSerializer


class ActaViewSet(viewsets.ModelViewSet):
    queryset = Acta.objects.all()
    serializer_class = ActaSerializer


class ComiteElectoraViewSet(viewsets.ModelViewSet):
    queryset = ComiteElectora.objects.all()
    serializer_class = ComiteElectoraSerializer


class VotoViewSet(viewsets.ModelViewSet):
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer


class ListaViewSet(viewsets.ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer
