from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
from . import forms,models
import datetime
from datetime import timedelta
import pytz
from googleapiclient import discovery
from googleapiclient.discovery import build
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2 import service_account
from decouple import config
from google.oauth2 import service_account
import googleapiclient.discovery
import datetime

import sys

def home(request):
    return render(request,"home.html")
def signup_view(request):
    if request.method=='POST':
        Domain=request.POST.get('domain')
        use = domain.objects.create(domain=Domain);
        use.save()
        print(Domain)        
        if(Domain=='Doctor'):
             print("Doctor");
             return HttpResponseRedirect('doctorsignup')
        else:
            print("Patient");
            return HttpResponseRedirect('patientsignup')
    return render(request,"signup.html")

def doctor_signup_view(request):
    userForm=forms.DoctorUserForm()
    doctorForm=forms.DoctorForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorForm(request.POST,request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor=doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
            return HttpResponseRedirect('login')
        else:
            messages.warning(request,'Password do not match')
            return redirect('doctorsignup')
    return render(request,'doctorsignup.html',context=mydict)

def patient_signup_view(request):
    userForm=forms.PatientUserForm()
    patientForm=forms.PatientForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        patientForm=forms.PatientForm(request.POST,request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.user=user
            patient.assignedDoctorId=request.POST.get('assignedDoctorId')
            patient=patient.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
            return HttpResponseRedirect('login')
        else:
            messages.warning(request,'Password do not match')
            return redirect('patientsignup')
    return render(request,'patientsignup.html',context=mydict)
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()
def afterlogin_view(request):
    if is_doctor(request.user):
            return redirect('doctor')
    elif is_patient(request.user):
            return redirect('patient')

@login_required(login_url='login')
@user_passes_test(is_patient)
def patient(request):
    patient=Patient.objects.all()
    patientt=Patient.objects.get(user_id=request.user.id)
    context={
    'patient':patient,
    'patientt':patientt
    }
    return render(request,'patient.html',context)
@login_required(login_url='login')   
@user_passes_test(is_doctor) 
def doctor(request):
    doctor=models.Doctor.objects.all()
    doctort=Doctor.objects.get(user_id=request.user.id)
    mydict={
    'doctor':doctor,
    'doctort':doctort
    }
    return render(request,'doctor.html',mydict)



def upload(request):
    uploadForm=forms.uploadForm()
    myd={'uploadForm':uploadForm}
    if request.method=='POST':
        uploadForm=forms.uploadForm(request.POST,request.FILES)
        if uploadForm.is_valid():
            user=uploadForm.save()
            user.save()
            return HttpResponseRedirect('upload')
    return render(request,"upload.html",context=myd)

def viewp(request):
    vie=formsss.objects.all()
    print(vie)
    mydict={
    'vie':vie
    }
    return render(request,"view.html", mydict)

def viewww(request):
    vi=formsss.objects.all().filter(Draft='No')
    mydict={
    'vi':vi
    }
    return render(request,'viewww.html', mydict)
def dbook(request):
    doctor=models.Doctor.objects.all()
    mydict={
    'doctor':doctor
    }
    return render(request,'doc.html',mydict)



start_time =0
end_time=0
  
scopes = ['https://www.googleapis.com/auth/calendar']

credentials = pickle.load(open('E:\\intern\\hos\\token.pkl', 'rb'))
def book(request,pk):
    form = Doctor.objects.get(id=pk)
    num=pk
    if request.method == 'POST':
        form = Doctor.objects.get(id=pk)
        req = request.POST['req']
        start = request.POST['start']
        time = request.POST['time']
        email = request.POST['email']
        starts = start +' '+ time +':' '00'
    
        start_time = datetime.datetime.strptime(starts,"%Y-%m-%d %H:%M:%S")
        end_time  = start_time + timedelta(minutes=45)
        context = { 'req':req,'start':start,'time':time,'start_time':start_time, 'end_time':end_time,'email':email,'form':form}
        contacttuber = Book(patientId=request.user.id,doctorId=num,patientName=request.user.username,doctorName=form.user.username,require=req,start_time=start_time,end_time=end_time) 
        contacttuber.save()
        return  render(request, 'confirm.html',context)
        

    
    return render(request,'book.html',{'form':form})

def confirm(request):
    if request.method == 'POST':
        req = request.POST['required']
        start = request.POST['starts']
        time = request.POST['time']
        email = request.POST['email']
        start = start +' '+ time +':' '00' 
        start_time = datetime.datetime.strptime(start,"%Y-%m-%d %H:%M:%S")
        end_time  = start_time + timedelta(minutes=45)
        timezone = 'Asia/Kolkata'
        
        return HttpResponseRedirect("patient")
    
    return render(request,'confirm.html')

def bookview(request):
    view=Book.objects.get(patientId=request.user.id)
    mydict={
    'view':view
    }
    return render(request,'bookview.html',mydict)
def bookvieww(request):
    view=Book.objects.all()
    mydict={
    'view':view
    }
    return render(request,'bookvieww.html',mydict)