from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError

# Регистрация пользователя
class RegisterView(APIView):
    permission_classes = [AllowAny]  # Разрешает доступ всем пользователям (независимо от авторизации)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({'message': 'Error saving user', 'errors': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Логин пользователя
class LoginView(APIView):
    permission_classes = [AllowAny]  # Разрешает доступ всем пользователям (независимо от авторизации)
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Использование authenticate для проверки логина и пароля
        user = authenticate(username=username, password=password)
        
        if user is not None:
            return Response({
                'message': 'Login successful', 
                'user': {
                    'username': user.username,
                    'email': user.email  # Можно также передавать другие данные, если нужно
                }
            }, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

# Главная страница
def home(request):
    return HttpResponse("Welcome to the home page!")
