from unittest.util import _MAX_LENGTH
from django.db import models
from multiselectfield import MultiSelectField
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class domain(models.Model):
    domain=models.CharField(max_length=100, null=True, blank=True)




departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]
class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)




class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

categories=[('Mental Health ','Mental Health '),
('Heart Disease','Heart Disease'),
('Covid','Covid'),
('Immunization','Immunization')
]
choi=[('Yes','Yes'),('No','No')]
class formsss(models.Model):
    Title=models.CharField(max_length=20)
    image= models.ImageField(upload_to='profile_pic/blogimage/',null=True,blank=True)
    catg= models.CharField(max_length=50,choices=categories,default='Covid')
    summary=models.TextField(max_length=150)
    content=models.TextField(max_length=300)
    Draft=models.CharField(max_length=20,choices=choi,default='No')

class Book(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    require = models.CharField(max_length=200,null=True)
    start_time = models.DateField()
    end_time = models.TimeField()