from django import forms
from django.forms import ModelForm
from .models import *
from datetime import datetime

class studentForm(ModelForm):
	class Meta:
		model=student
		widgets={ 'password':forms.PasswordInput() }
		fields = "__all__"
class loginForm(forms.Form):
	roll_no=forms.CharField(max_length=20,help_text="enter your roll no.")
	password=forms.CharField(max_length=20,widget=forms.PasswordInput())
class complaintForm(ModelForm):
	class Meta:
		model=dummy
		fields=('comp_type','hall','room','mobile','comment')
		#fields="__all__"

class admin_loginForm(forms.Form):
	user_name=forms.CharField(max_length=20,help_text="enter your user_name")
	password=forms.CharField(max_length=20,widget=forms.PasswordInput())