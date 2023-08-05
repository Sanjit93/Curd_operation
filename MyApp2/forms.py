from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ("name","email","mob_no")
        widgets ={
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'mob_no' : forms.TextInput(attrs={'class' : 'form-control'}),
            
        }

