from django import forms
from django.forms import ModelForm
from .models import *
from datetime import datetime

class studentForm(ModelForm):
	class Meta:
		model=student
		widgets={ 'password':forms.PasswordInput() }
		fields = "__all__"