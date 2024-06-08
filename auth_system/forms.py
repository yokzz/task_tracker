from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput

class SignUpForm(UserCreationForm):
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
    
    password1 = forms.CharField(
        label='Password 1',
        widget=forms.PasswordInput(
            attrs = {
                'class': "form-control rounded-3",
                'id': "password1",
                'placeholder': 'Password 1',
            }
        )
    )
    
    password2 = forms.CharField(
        label='Password 2',
        widget=forms.PasswordInput(
            attrs = {
                'class': "form-control rounded-3",
                'id': "password2",
                'placeholder': 'Password 2',
            }
        )
    )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']    
        
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
    
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
        widget=forms.PasswordInput(
            attrs = {
                'class': "form-control rounded-3",
                'id': "password",
                'placeholder': 'Password',
            }
        )
    )
