from django.db import models
from django.contrib.auth.models import User

class Donormodel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='donor/images',null=True,blank=True)
    bloodgroup = models.CharField(max_length=10)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

DONATE_STATUS = [
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
]

class BloodDonate(models.Model): 
    donor = models.ForeignKey(User,on_delete=models.CASCADE)   
    age = models.PositiveIntegerField()
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=DONATE_STATUS, default="Pending")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.donor.user.username