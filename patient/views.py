from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.

class Patientviewset(viewsets.ModelViewSet):
    queryset = models.Patientmodel.objects.all()
    serializer_class = serializers.PatientSerializer
