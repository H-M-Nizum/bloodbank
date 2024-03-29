from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register('list', views.Donorviewset)
router.register('donatlist', views.BloodDonateviewset)

urlpatterns = [
    path('', include(router.urls))
]
