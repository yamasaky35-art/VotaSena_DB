from django.shortcuts import render
from rest_framework import viewsets

from .models import Ficha, Jornada, ProgramaFormacion, ProgramaSede, Rol
from .serializers import (
    FichaSerializer,
    JornadaSerializer,
    ProgramaFormacionSerializer,
    ProgramaSedeSerializer,
    RolSerializer,
)


class ProgramaFormacionViewSet(viewsets.ModelViewSet):
    queryset = ProgramaFormacion.objects.all()
    serializer_class = ProgramaFormacionSerializer


class ProgramaSedeViewSet(viewsets.ModelViewSet):
    queryset = ProgramaSede.objects.all()
    serializer_class = ProgramaSedeSerializer


class JornadaViewSet(viewsets.ModelViewSet):
    queryset = Jornada.objects.all()
    serializer_class = JornadaSerializer


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


class FichaViewSet(viewsets.ModelViewSet):
    queryset = Ficha.objects.all()
    serializer_class = FichaSerializer
