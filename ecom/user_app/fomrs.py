from django import forms
from . models import UserInfo
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserInfo
        fields = ["first_name", "last_name", "email", "username", "password1", "password2", "gender", "address", "city", "pincode", "phone_no"]

    def email_clean(self):
        email = self.cleaned_data["email"]
        user = UserInfo.objects.filter(email=email)
        if user:
            raise ValidationError(" Email Already Exist")
        return email


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
