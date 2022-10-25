from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput
from .models import todo

class Register(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','date_joined']
class Signin(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
class person_list(forms.ModelForm):
    class Meta:
        model=todo
        fields=["Title","Note","Last_Date","Status","Count"]