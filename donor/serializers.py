from rest_framework import serializers
from . import models

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Donormodel
        fields = '__all__'


class BloodDonateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BloodDonate
        fields = '__all__'