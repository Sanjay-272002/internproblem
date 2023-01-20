from  django.urls import path
from .import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns =[
   path('',views.home, name="home"),
   path('signup',views.signup_view,name="signup"),
   path('login',LoginView.as_view(template_name='signin.html'),name="login"),
   path('doctorsignup', views.doctor_signup_view,name='doctorsignup'),
   path('patientsignup', views.patient_signup_view,name='patientsignup'),
   path('doctor', views.doctor,name='doctor'),
   path('patient', views.patient,name='patient'),
   path('afterlogin', views.afterlogin_view,name='afterlogin'),
   path('logout', LogoutView.as_view(template_name='home.html'),name='logout'),
   path('upload',views.upload,name='upload'),
   path('viewp',views.viewp,name='viewp'),
   path('viewww',views.viewww,name='viewww'),
]