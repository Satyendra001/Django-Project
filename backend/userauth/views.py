from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
        
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class SignUp(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            if User.objects.filter(username=username).exists():
                return Response({"response" : {'error':'User already exists'}})
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
            
            return Response({"response":{"success":"User created"}})
        except:
            return Response({"response":{"error":"Some error occured"}})

