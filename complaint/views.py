from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *
from .models import *
# Create your views here.

def home(request):
<<<<<<< HEAD
	return render(request,"base.html",{})
=======
	return render(request,'index.html',{})
def signup(request):
	if(request.method=='POST'):
		form=studentForm(request.POST)
		if(form.is_valid()):
			ins=student()
			ins.roll=form.cleaned_data['roll']
			ins.name=form.cleaned_data['name']
			ins.hall=form.cleaned_data['hall']
			ins.gender=form.cleaned_data['gender']
			ins.mobile=form.cleaned_data['mobile']
			ins.email=form.cleaned_data['email']
			ins.password=form.cleaned_data['password']
			ins.room=form.cleaned_data['room']
			ins.save()
			return HttpResponseRedirect('/')
	else:
		form=studentForm()
	return render(request,'signup.html',{'form':form})
>>>>>>> 359c76260b56925ad74fad35b62e6f5e389653a8
