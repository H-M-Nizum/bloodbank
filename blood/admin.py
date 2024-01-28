from django.contrib import admin
from . models import Stock, BloodRequest
# Register your models here.

admin.site.register(Stock)


class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ['patient_username', 'donor_name', 'patient_age', 'unit', 'reason', 'bloodgroup', 'date']

    def donor_name(self, obj):
        return obj.request_by_donor.user.username
    def patient_username(self, obj):
        return obj.request_by_patient.user.username
admin.site.register(BloodRequest, BloodRequestAdmin)