from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.

class Donorviewset(viewsets.ModelViewSet):
    queryset = models.Donormodel.objects.all()
    serializer_class = serializers.DonorSerializer

