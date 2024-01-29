from django.contrib import admin
from .models import Patientmodel, ContactUsModel
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'age', 'bloodgroup', 'mobile']

    # Get Relational fields data (forignkey, onetoonefield, manytomany fields)
    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name
    
    def email(self, obj):
        return obj.user.email

admin.site.register(Patientmodel, PatientAdmin)

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'message']

admin.site.register(ContactUsModel, ContactUsAdmin)