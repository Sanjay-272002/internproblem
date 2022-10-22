from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import GeeksForm 


def home(request):
    return render(request,"home.html")


def patient(request):
     return render(request,"patient.html")
    
def doctor(request):
    return render(request,"doctor.html")

def register(request):
     if request.method == 'POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        selectimage=request.POST.get('sanjay')
        domain=request.POST.get('profession')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')

        if password == confirm_password:
            if Contact.objects.filter(username=username).exists():

                print("not valid")
                return redirect('doctor')
            else:
                if Contact.objects.filter(email=email).exists():
                    print("email")
                    return redirect('register')
                else:
                    register = Contact.objects.create(firstname=firstname, lastname=lastname,username=username,profileimg=selectimage,category=domain, email=email, password=password,address=address,city=city,state=state,pincode=pincode)
                    register.save()
                    
                    print("user saved")
                    return  redirect('home')
                    
        else:
            
            return redirect('patient')

     return render(request,"signup.html")

def login_user(request):
    if request.method == 'POST':
        if Contact.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            register = Contact.objects.get(username=request.POST['username'], password=request.POST['password'])
            domain=request.POST.get('profession')
            if (domain=="Doctor"):
                return render(request, 'doctor.html', {'register': register})
            else:
                return render(request, 'patient.html', {'register': register})

        else:
            
            return render(request, 'login.html')
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']

    #     register = authentication(request, username=username)

    #     if register is not None:
    #         login(request, register)
           
    #         return redirect('doctor') 
    #     else:
           
    #         return redirect('home') 
    
    return render(request,"signin.html")
    
# def create(request):
    form = GeeksForm()
    if request.method == 'POST':
        form = GeeksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor')

    context = { 'form':form }
    return render(request, 'create.html', context)
 
 
def read(request):
    user_data = Contact.objects.all()
   
    context = { 'user_data': user_data, }
    return render(request, 'doctor.html', context)