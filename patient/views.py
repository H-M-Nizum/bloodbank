from django.shortcuts import render, redirect
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

# for sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from rest_framework.authtoken.models import Token

from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated  



class Patientviewset(viewsets.ModelViewSet):
    queryset = models.Patientmodel.objects.all()
    serializer_class = serializers.PatientSerializer

class patientRegisterViewsset(APIView):
    serializer_class = serializers.PatientRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            # print(user)
            # print(user.email)

            token = default_token_generator.make_token(user)
            # print('token', token)

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            # print(uid)

            confirm_link = f"https://lifesafe-bank.onrender.com/patient/active/{uid}/{token}"

            email_subject = 'Çonfirm your email'
            email_body = render_to_string('email.html', {'confirm_link' : confirm_link})
            
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response(" Check Your mail for confirmation")
        return Response(serializer.errors)



def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except (user.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect("login")
    else:
        return redirect("register")




class UserLoginApiview(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({'token': token.key, 'úser_id': user.id})
            else:
                return Response({'error' : 'Invalid User'})

        return Response(serializer.errors)


class UserLogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect("login")




class AdminLoginApiview(APIView):
    def post(self, request):
        serializer = serializers.AdminLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            if user and user.is_superuser:
                login(request, user)
                return Response('successful')
            else:
                return Response({'error': 'Invalid User'})

        return Response(serializer.errors)



class AdminLogoutAPIView(APIView):
    def get(self, request):
        logout(request)
        return redirect("adminlogin")

class ContactAPIView(APIView):
    serializer_class = serializers.ContactUsSerializers
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            phone = serializer.validated_data['phone']
            message = serializer.validated_data['message']
            print(name, email, phone, message)

            email_subject = "Contact email"
            email_body = render_to_string('mail.html', {'name':name, 'from_email':email, 'message':message, 'phone': phone})

            email = EmailMultiAlternatives(email_subject, '', email, to=['hmnizum1714032@gmail.com'])
            email.attach_alternative(email_body, "text/html")
            email.send()

            
            return Response(" Message Sent Successfully!")
        return Response(serializer.errors)
