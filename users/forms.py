from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterationForm(UserCreationForm):
    emails = forms.EmailField()
    
    class Meta:
        model = User,
        field = ['username', 'email', 'password1', 'password2']