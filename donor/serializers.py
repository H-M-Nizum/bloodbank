from rest_framework import serializers
from . import models

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Donormodel
        fields = '__all__'