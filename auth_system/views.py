from django.shortcuts import render, redirect
from auth_system.forms import SignUpForm, LoginForm, UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy

class SignUpView(CreateView):
    template_name = "auth_system/signup.html"
    form_class = SignUpForm
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse_lazy("auth_system:login"))
    
    
class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = "auth_system/login.html"
    

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy("auth_system:login"))