from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register('list', views.Patientviewset)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.patientRegisterViewsset.as_view(), name='register'), 
    path('login/', views.UserLoginApiview.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('adminlogin/', views.AdminLoginApiview.as_view(), name='adminlogin'),
    path('adminlogout/', views.AdminLogoutAPIView.as_view(), name='adminlogout'),
    path('active/<uid64>/<token>/', views.activate, name='activate'),
    path('contact/', views.ContactAPIView.as_view(), name='contact'),
]
