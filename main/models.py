from unittest.util import _MAX_LENGTH
from django.db import models
from multiselectfield import MultiSelectField
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    profileimg=models.ImageField(upload_to='profile_images')
    category = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    password=models.CharField(max_length=100, null=True, blank=True)
    confirmpassword=models.CharField(max_length=100, null=True, blank=True)
    address=models.TextField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.BigIntegerField()
    

    def __str__(self):
        return self.name