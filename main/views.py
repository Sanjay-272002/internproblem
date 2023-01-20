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
    context={
    'patient':patient
    }
    return render(request,'patient.html',context)
    
@user_passes_test(is_doctor) 
def doctor(request):
    doctor=models.Doctor.objects.all()
    mydict={
    'doctor':doctor
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
