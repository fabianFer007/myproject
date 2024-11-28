from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Usa el modelo CustomUser
        fields = ['username', 'email']  # Define los campos que quieres usar
