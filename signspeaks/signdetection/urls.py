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
    path("update_profile/",views.update_profile, name="update_profile"),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset/<uidb64>/<token>/', views.reset_password, name='reset_password'),
    path('password_reset_done/', views.password_reset_done, name='password_reset_done'),

    path('token' , views.token_send , name="token_send"),
    path('success' , views.success , name='success'),
    path('verify/<auth_token>' , views.verify , name="verify"),

    path('recognition/', views.recognition, name='recognition'),
    path('video_feed/', views.video_feed, name='video_feed'),


]
