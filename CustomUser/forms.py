from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs = {
        'class':"form-control",
        "placeholder":"Enter your username"
    }))
    password1 = forms.CharField(widget = forms.TextInput(attrs = {
        'class':"form-control",
        "placeholder":"Enter your password"
    }))
    password2 = forms.CharField(widget = forms.TextInput(attrs = {
        'class':"form-control",
        "placeholder":"confrim your password"
    }))


    class Meta:
        model = User
        fields = 'username',
        field_classes = {'username': UsernameField}