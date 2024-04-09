from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class StaffSignupForm(UserCreationForm):
    email = models.EmailField(max_length=255, null=True)    
    profile_image = forms.ImageField(required=False)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2','profile_image']


        
class StudentSignupForm(UserCreationForm):
    email = models.EmailField(max_length=255, null=True)    
    profile_image = forms.ImageField(required=False)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2','profile_image']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
