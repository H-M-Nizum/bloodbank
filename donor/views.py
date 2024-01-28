from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.

class Donorviewset(viewsets.ModelViewSet):
    queryset = models.Donormodel.objects.all()
    serializer_class = serializers.DonorSerializer


class BloodDonateviewset(viewsets.ModelViewSet):
    queryset = models.BloodDonate.objects.all()
    serializer_class = serializers.BloodDonateSerializer

    # custom query
    def get_queryset(self):
        queryset = super().get_queryset()
        donor_id = self.request.query_params.get('donor_id')

        if donor_id:
            queryset = queryset.filter(donor_id = donor_id)
        return queryset
    

