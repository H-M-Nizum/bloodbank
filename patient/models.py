from django.db import models
from django.contrib.auth.models import User

class Patientmodel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='Patient/images',null=True,blank=True)

    age = models.PositiveIntegerField()
    bloodgroup = models.CharField(max_length=10)
    disease = models.CharField(max_length=100)
    doctorname = models.CharField(max_length=50)

    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
   
  
    def __str__(self):
        return self.user.first_name+ " " + self.user.last_name