from django.contrib import admin
from django.urls import path
from . views import *

urlpatterns = [
    path("login/", UserloginView.as_view(), name="login"),
    path("registration/", UserRegistrationView.as_view, name='registration')
]