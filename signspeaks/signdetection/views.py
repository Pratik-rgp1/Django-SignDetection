from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.contrib import messages
from django.contrib.auth import logout as auth_logout

from .forms import NewUserForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = NewUserForm()
    return render(request, "users/register.html", {"register_form": form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('homepage')  
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Use the renamed function
                return redirect("homepage")
    else:
        form = AuthenticationForm()
    return render(request=request, template_name="users/login.html", context={"login_form": form})
	

def forget_password(request):
    return render(request,'users/forget_password.html')

def homepage(request):
    return render(request,'homepage.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')
