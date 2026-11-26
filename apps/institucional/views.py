from django.shortcuts import render
from rest_framework import viewsets

from .models import BienestarAprendiz, CentroFormacion, Sede
from .serializers import (
    BienestarAprendizSerializer,
    CentroFormacionSerializer,
    SedeSerializer,
)


class CentroFormacionViewSet(viewsets.ModelViewSet):
    queryset = CentroFormacion.objects.all()
    serializer_class = CentroFormacionSerializer


class BienestarAprendizViewSet(viewsets.ModelViewSet):
    queryset = BienestarAprendiz.objects.all()
    serializer_class = BienestarAprendizSerializer


class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer

# Create your views here.
