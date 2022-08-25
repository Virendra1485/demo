from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserInfo(User):
    GENDER = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]

    ROLE = [
        ('customer', 'Customer'),
        ('seller', 'Seller'),
        ('admin', 'Admin')
    ]
    gender  = models.CharField(choices=GENDER, max_length=50)
    address = models.TextField()
    city = models.CharField(max_length=100) 
    pincode = models.CharField(max_length=6)
    phone_no = models.CharField(unique=True, max_length=12)
    role = models.CharField(choices=ROLE, max_length=100, default='Customer')