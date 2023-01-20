from django import forms
from django.contrib.auth.models import User
from . import models


class DoctorUserForm(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']
        widgets = {
        'password': forms.PasswordInput()
        }
    def clean(self):
        cleaned_data = super(DoctorUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
class DoctorForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields=['address','status','profile_pic']
class PatientUserForm(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']
        widgets = {
        'password': forms.PasswordInput()
        }
    def clean(self):
        cleaned_data = super(PatientUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
class PatientForm(forms.ModelForm):
    class Meta:
        model=models.Patient
        fields=['address','status','profile_pic']

class uploadForm(forms.ModelForm):
    class Meta:
        model=models.formsss
        fields=['Title','image','catg','summary','content','Draft']