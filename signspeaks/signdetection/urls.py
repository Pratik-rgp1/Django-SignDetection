from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.homepage, name="homepage"),
    path("aboutus/",views.aboutus, name="aboutus"),
    path("contactus/",views.contactus, name="contactus"),
    
    path("register/",views.register, name="register"),
    path("login/",views.user_login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
