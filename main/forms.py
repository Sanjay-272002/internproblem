from django import forms
from .models import Contact
 
 
# creating a form
class GeeksForm(forms.ModelForm):
 
   
    class Meta:
        
        model = Contact

        fields = [
            "firstname",
            "lastname",
            "username",
            "category",
            "email",
            "state",

        ]