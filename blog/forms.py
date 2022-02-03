from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import contact,User_blog
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

#contact form
class Usercontact(forms.ModelForm):
  class Meta:
    model = contact
    fields = ['id','name','email','mobile','messages']
    widgets = {
      "name":forms.TextInput(attrs={'class':'form-control','placeholder':'Please Enter Your Name'}),
      "email":forms.EmailInput(attrs={'class':'form-control','placeholder':'Please Enter Your Email'}),
      "mobile":forms.NumberInput(attrs={'class':'form-control','placeholder':'Please Enter Your Mobile Number'}),
      "messages":forms.TextInput(attrs={'class':'form-control','placeholder':'Please Enter Your Description'})
    }

#signup form
class UserAdminCreationForm(UserCreationForm):
  password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
  password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
  class Meta:
    model = get_user_model()
    fields = ['email','first_name','last_name']
    labels = {'first_name':'First Name','last_name':'Last Name'}
    widgets = {
      "email":forms.EmailInput(attrs={'class':'form-control'}),
      "first_name":forms.TextInput(attrs={'class':'form-control'}),
      "last_name":forms.TextInput(attrs={'class':'form-control'}),
    }

#login form
class LoginForm(AuthenticationForm):
  username = UsernameField(widget = forms.EmailInput(attrs={'class':'form-control','type':'email'}))
  password = forms.CharField(widget = forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

#blog form
class Userblog(forms.ModelForm):
  class Meta:
    model = User_blog
    fields = ['id','title','des']
    labels = {"des":'Description'}
    widgets = {
      "title":forms.TextInput(attrs={'class':'form-control','placeholder':'Please Enter Your Name'}),
      "des":forms.Textarea(attrs={'class':'form-control','placeholder':'Please Enter Your Description'}),
    }
