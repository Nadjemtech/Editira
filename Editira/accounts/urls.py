from typing import Pattern
from django.contrib.auth import logout
from django.urls import include, path
from .views import  CheckNote, Login, Logout, clientProfile ,RegisterView
app_name='accounts'

urlpatterns = [
    path('Client/<int:pk>/', clientProfile, name='cProfile'),
    path('Client/note-checker/<int:nt>/', CheckNote, name='Check'),
    path('Login/',Login , name='Login'),
    path('Logout/', Logout, name='Logout'),
    path('Register/', RegisterView , name='register'),
]