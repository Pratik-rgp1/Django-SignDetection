from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

from django.template import Context

from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("signspeaks:homepage")
        else:
            print(form.errors)  # Print form errors to console for debugging
            messages.error(request, "Unsuccessful registration. Please correct the errors.")
    else:
        form = NewUserForm()
    return render(request=request, template_name="user/register.html", context={"register_form":form})


def homepage(request):
    return render(request,'homepage.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')
