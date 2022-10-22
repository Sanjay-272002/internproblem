from  django.urls import path

from .import views

urlpatterns =[
   path('',views.home, name="home"),
   path('patient',views.patient,name="patient"),
   path('doctor',views.doctor,name="doctor"),
   path('signup',views.register,name="register"),
   path('login_user',views.login_user, name="login"),
   
]