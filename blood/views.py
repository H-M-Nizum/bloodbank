from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.

class BloodStockviewset(viewsets.ModelViewSet):
    queryset = models.Stock.objects.all()
    serializer_class = serializers.BloodStockSerializer


class BloodRequestviewset(viewsets.ModelViewSet):
    queryset = models.BloodRequest.objects.all()
    serializer_class = serializers.BloodRequestSerializer

    # custom query
    def get_queryset(self):
        queryset = super().get_queryset()
        request_by_patient_id = self.request.query_params.get('request_by_patient_id')

        if request_by_patient_id:
            queryset = queryset.filter(request_by_patient_id = request_by_patient_id)
        return queryset