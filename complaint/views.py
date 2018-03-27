from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *
from .models import *
from .my_library import create_dynamic 
import importlib

# Create your views here.

def home(request):
	return render(request,'complaint/index.html',{})
def profile(request):
	user=""
	if 'user' in request.COOKIES:
		user=request.COOKIES['user']
		if(user=='NULL'):
			return HttpResponseRedirect('/log/')
	else:
		return HttpResponseRedirect('/log/')
	username=user.split("_")[1]
	ins=student.objects.get(roll=username)
	stu_name=ins.name
	stu_hall=ins.hall
	stu_room=ins.room
	stu_mobile=ins.mobile
	stu_email=ins.email
	stu_roll=ins.roll
	ins.save()
	module=importlib.import_module('complaint.models')
	class_=getattr(module,user)
	last_one=class_.objects.filter(status='Registered').order_by('-id')[:1]
	last_two=class_.objects.filter(status='seen')
	#print (len(list(last_one)))
	context={'name':stu_name,'hall':stu_hall,'room':stu_room,'mobile':stu_mobile,'email':stu_email,'roll_no':stu_roll,'detail':last_one}
	return render(request,'complaint/blog.html',context)



def contact(request):
	return render(request,'complaint/contact.html',{})
def logout(request):
	user=request.COOKIES['user']
	response=render(request,'complaint/index.html')
	if(user!='NULL'):
		user='NULL'
		response.set_cookie('user',user)
	return response
def register(request):
	user=""
	if 'user' in request.COOKIES:
		user=request.COOKIES['user']
		if(user=='NULL'):
			return HttpResponseRedirect('/log/')
	else:
		return HttpResponseRedirect('/log/')
	print ("form valid1")
	if(request.method=='POST'):
		form=complaintForm(request.POST)
		print ("print")
		if(form.is_valid()):
			print ("form valid")
			module=importlib.import_module('complaint.models')
			class_=getattr(module,user)
			ins=class_()
			dummy_ins=dummy()
			dummy_ins.comp_type=ins.comp_type=form.cleaned_data['comp_type']
			dummy_ins.hall=form.cleaned_data['hall']
			dummy_ins.room=form.cleaned_data['room']
			dummy_ins.mobile=form.cleaned_data['mobile']
			dummy_ins.comment=form.cleaned_data['comment']
			ins.save()
			comp_id=user.split('_')[1]
			comp_id=comp_id+"_"+str(ins.id)
			#ins.id=comp_id
			dummy_ins.comp_id=comp_id
			#ins.save()
			dummy_ins.save()
			return HttpResponse('Done')

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
	if('user' in request.COOKIES):
		user=request.COOKIES['user']
		if(user!='NULL'):
			return render(request,'complaint/logout.html',{})
	if(request.method=='POST'):
		form=loginForm(request.POST)
		if(form.is_valid()):
			roll_no=form.cleaned_data['roll_no']
			try:
				print(roll_no)
				ins=student.objects.get(roll=str(roll_no))
				print("Found")
				username="st_"+roll_no
				password=form.cleaned_data['password']
				if(ins.password==password):
					response=render(request,'complaint/index.html',{})
					response.set_cookie('user',username)
					return response
				else:
					var="Invalid Password"
					return render(request,'complaint/login.html',{'var':var})
			except:
				var="Invalid Roll No."
				return render(request,'complaint/login.html',{'var':var})

	else:
		form=loginForm()
	return render(request,'complaint/portfolio.html',{'form':form})




