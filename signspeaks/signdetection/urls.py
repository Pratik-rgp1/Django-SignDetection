from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage, name="homepage"),
    path("aboutus/",views.aboutus, name="aboutus"),
    path("contactus/",views.contactus, name="contactus"),
    path("registerpage",views.register, name="registerpage"),
    path("login",views.login, name="login")
]
