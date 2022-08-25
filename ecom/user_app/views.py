from django.shortcuts import render, redirect
from django.views import View
from . fomrs import *
# Create your views here.


class UserRegistrationView(View):
    context = {"form": UserRegistrationForm()}

    def get(self, request):
        return render(request, "home.html", self.context)

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("/user/login/")
        return render(request, "home.html", self.context)


class UserloginView(View):
    def get(self, request):
        return render(request, "login.html", self.context)
