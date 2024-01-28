from rest_framework import serializers
from . import models

class BloodStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stock
        fields = '__all__'

class BloodRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BloodRequest
        fields = '__all__'