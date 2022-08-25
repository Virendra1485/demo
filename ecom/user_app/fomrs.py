from dataclasses import fields
from django import forms
from . models import UserInfo


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model  = UserInfo
        fields = ["first_name", "last_name", "email", "username", "password", "gender", "address", "city", "pincode", "phone_no"]