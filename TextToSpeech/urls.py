"""TextToSpeech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TextToSpeech import views as mainView
from users import views as usr
from admins import views as admins

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", mainView.index, name='index'),
    path("workingProcess/", mainView.workingProcess, name='workingProcess'),
    path("index/", mainView.index, name="index"),
    path("logout/", mainView.logout, name="logout"),
    path("UserLogin/", mainView.UserLogin, name="UserLogin"),
    path("AdminLogin/", mainView.AdminLogin, name="AdminLogin"),
    path("UserRegister/", mainView.UserRegister, name="UserRegister"),

    ### User Side Views
    path("UserRegisterActions/", usr.UserRegisterActions, name="UserRegisterActions"),
    path("UserLoginCheck/", usr.UserLoginCheck, name="UserLoginCheck"),
    path("UserHome/", usr.UserHome, name="UserHome"),
    path("TextToSpeechForm/", usr.TextToSpeechForm, name='TextToSpeechForm'),
    path("GenerateSpeaksforUser/", usr.GenerateSpeaksforUser, name="GenerateSpeaksforUser"),
    path("UserSpeechData/", usr.UserSpeechData, name='UserSpeechData'),
    path("UserTimeDifference/", usr.UserTimeDifference, name="UserTimeDifference"),


    ### Admin Side Views
    path("AdminLoginCheck/", admins.AdminLoginCheck, name="AdminLoginCheck"),
    path("AdminHome/", admins.AdminHome, name="AdminHome"),
    path("ViewRegisteredUsers/", admins.ViewRegisteredUsers, name="ViewRegisteredUsers"),
    path("AdminActivaUsers/", admins.AdminActivaUsers, name="AdminActivaUsers"),
    path("AdminViewSpeechData/", admins.AdminViewSpeechData, name="AdminViewSpeechData"),
    path("AdminViewTimeDifference/", admins.AdminViewTimeDifference, name="AdminViewTimeDifference"),



]
