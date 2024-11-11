
# base/urls.py
from .views import home
from django.urls import path
from django.contrib import admin
from .views import RegisterView, LoginView

urlpatterns = [
   
    path('', home, name='home'),  # Это маршрут для корневой страницы
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
