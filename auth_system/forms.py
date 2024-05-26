from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control rounded-3",
                'id': "username",
                'placeholder': 'Username',
                }),
            
            'password': PasswordInput(attrs={
                'class': "form-control rounded-3",
                'id': "password",
                'placeholder': 'Password',
                }),
        }
        
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs = {
                'class': "form-control rounded-3",
                'id': "username",
                'placeholder': 'Username',
            }
        )
    )
    
    password = forms.CharField(
        label='Password',
        widget=forms.TextInput(
            attrs = {
                'class': "form-control rounded-3",
                'id': "password",
                'placeholder': 'Password',
            }
        )
    )
