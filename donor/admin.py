from django.contrib import admin
from .models import Donormodel, BloodDonate
# Register your models here.

class DonorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'address', 'bloodgroup', 'mobile']

 
    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name
    
    def email(self, obj):
        return obj.user.email

admin.site.register(Donormodel, DonorAdmin)

class BloodDonateAdmin(admin.ModelAdmin):
    list_display = ['username', 'age', 'unit', 'status', 'bloodgroup', 'date']

    def username(self, obj):
        return obj.donor.user.username

    

admin.site.register(BloodDonate, BloodDonateAdmin)