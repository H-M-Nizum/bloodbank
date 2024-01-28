from rest_framework import serializers
from . import models

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patientmodel
        fields = '__all__'