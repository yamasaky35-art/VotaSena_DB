from django.shortcuts import render
from rest_framework import viewsets

from .models import Aprendiz, CandidatoPostulado, Persona
from .serializers import AprendizSerializer, CandidatoPostuladoSerializer, PersonaSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class AprendizViewSet(viewsets.ModelViewSet):
    queryset = Aprendiz.objects.all()
    serializer_class = AprendizSerializer


class CandidatoPostuladoViewSet(viewsets.ModelViewSet):
    queryset = CandidatoPostulado.objects.all()
    serializer_class = CandidatoPostuladoSerializer
