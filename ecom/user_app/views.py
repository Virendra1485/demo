from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .fomrs import *


# Create your views here.


class UserRegistrationView(View):
    context = {"form": UserRegistrationForm()}

    def get(self, request):
        return render(request, "home.html", self.context)

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/user/login/")
        return render(request, "home.html", {"form": form})


class UserLoginView(View):
    context = {"form": UserLoginForm()}

    def get(self, request):
        return render(request, "login.html", self.context)

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect("/home/")
        return render(request, "login.html", self.context)
