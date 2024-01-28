from django.db import models
from patient.models import Patientmodel
from donor.models import Donormodel

class Stock(models.Model):
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.bloodgroup

DONATE_STATUS = [
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
]
class BloodRequest(models.Model):
    request_by_patient = models.ForeignKey(Patientmodel, null=True,on_delete=models.CASCADE)
    request_by_donor = models.ForeignKey(Donormodel,null=True,on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=30)
    patient_age = models.PositiveIntegerField()
    reason = models.CharField(max_length=500)
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20,  choices=DONATE_STATUS, default="Pending")
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.bloodgroup

        