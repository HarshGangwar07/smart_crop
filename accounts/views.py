from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import LoginSerializer
from rest_framework import serializers

# Create your views here.
class LoginAPIView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({'message' : 'Login successful'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RegisterAPIView(APIView):
    class RegisterSerializer(serializers.ModelSerializer):
        password = serializers.CharField(write_only=True)

        class Meta:
            model = User
            fields = ['username', 'email', 'password']
        
        def create(self, validated_data):
            user = User.objects.create_user(
                username = validated_data['username'],
                email = validated_data['email'],
                password = validated_data['password'],  
            )
            return user
        def post(self, request):
            serializer = self.RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message' : 'User registered succesfully'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
