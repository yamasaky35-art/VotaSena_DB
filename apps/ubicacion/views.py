from django.shortcuts import render
from rest_framework import viewsets

from .models import Departamento, Municipio
from .serializers import DepartamentoSerializer, MunicipioSerializer


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
