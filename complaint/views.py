from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *
from .models import *
from .my_library import create_dynamic 
# Create your views here.

def home(request):
	return render(request,'complaint/index.html',{})
def profile(request):
	return render(request,'complaint/blog.html',{})
def contact(request):
	return render(request,'complaint/contact.html',{})
def register(request):
	if(request.method=='POST'):
		form=complaintForm()
		if(form.is_valid()):

			ins.comp_type=form.cleaned_data['comp_type']
			ins.hall=form.cleaned_data['hall']
			ins.room=form.cleaned_data['room']
			ins.mobile=form.cleaned_data['mobile']
			ins.comment=form.cleaned_data['comment']
			ins.save()
	else:
		form=complaintForm()
	return render(request,'complaint/services.html',{'form':form})

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
			st="st_"+str(ins.roll)
			create_dynamic(st)
			return HttpResponseRedirect('/')
	else:
		form=studentForm()
	return render(request,'complaint/signup.html',{'form':form})

def login(request):
	if(request.method=='POST'):
		form=loginForm(request.POST)
		if(form.is_valid()):
			roll_no=form.cleaned_data['roll_no']
			try:
				ins=student.objects.get(roll_no=roll_no)
				password=form.cleaned_data['password']
				if(ins.password==password):
					
					return render(request,'complaint/index.html',{})
				else:
					var="Invalid Password"
					return render(request,'complaint/login.html',{'var':var})
			except:
				var="Invalid Roll No."
				return render(request,'complaint/login.html',{'var':var})

	else:
		form=loginForm()
	return render(request,'complaint/portfolio.html',{'form':form})




