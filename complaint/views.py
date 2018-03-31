from .send_mail_to_reciept import send_mail_to
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *
from .models import *
import random
from .my_library import create_dynamic 
import importlib
from django.db.models import Q
import queue
from multiprocessing import Process

# Create your views here.

def home(request):
	
	return render(request,'complaint/index.html',{})
def profile(request):
	module=importlib.import_module('complaint.models')
	user=""
	if 'user' in request.COOKIES:
		user=request.COOKIES['user']
		if(user=='NULL'):
			return HttpResponseRedirect('/log/')
	else:	
		return HttpResponseRedirect('/log/')
	class_=getattr(module,user)
	if(request.method=='POST'):
		form=otp_form(request.POST)
		if form.is_valid():
			otp=form.cleaned_data['otp']
			try:
				attribute=dummy.objects.get(otp=otp)
				attribute.status="Completed"
				attribute.save()
				comp_iden=attribute.comp_id
				comp_iden=comp_iden.split("_")[1]
				attri=class_.objects.get(id=comp_iden)
				attri.status="Completed"
				attri.save()
			except:
				pass
	username=user.split("_")[1]
	ins=student.objects.get(roll=username)
	stu_name=ins.name
	stu_hall=ins.hall
	stu_room=ins.room
	stu_mobile=ins.mobile
	stu_email=ins.email
	stu_roll=ins.roll
	ins.save()
	#last_one=class_.objects.filter(status='Registered').order_by('-id')[:1]
	last_reg=class_.objects.filter(status='Registered')
	last_seen=class_.objects.filter(status='seen')
	last_ass=class_.objects.filter(status='Assigned')
	#print (len(list(last_one)))
	form=otp_form()
	context={'form':form,'name':stu_name,'hall':stu_hall,'room':stu_room,'mobile':stu_mobile,'email':stu_email,'roll_no':stu_roll,'detail_reg':last_reg,'detail_seen':last_seen,'detail_ass':last_ass}
	return render(request,'complaint/blog.html',context)
def admin_login(request):
	if(request.method=='POST'):
		form=admin_loginForm(request.POST)
		if(form.is_valid()):
			Admin_name=form.cleaned_data['user_name']
			try:
				#print(roll_no)
				ins=admin_people.objects.get(user_name=Admin_name)
				print("Found")
				password=form.cleaned_data['password']
				if(ins.password==password):
					return render(request,'complaint/admin_base.html',{})
				else:
					var="Invalid Password"
					return render(request,'complaint/admin_login.html',{'form':form,'var':var})
			except:
				var="Invalid Admin Username"
				return render(request,'complaint/admin_login.html',{'form':form,'var':var})

	else:
		form=admin_loginForm()
	return render(request,'complaint/admin_login.html',{'form':form})

def admin_profile(request):
	return render(request,'complaint/admin_profile')

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
			new_otp=0
			while True:
				new_otp=random.randint(1000,9999)
				try:
					otp.objects.get(otp_number=new_otp)
					continue
				except:
					break
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
			dummy_ins.otp=new_otp
			ins.save()
			comp_id=user.split('_')[1]
			comp_id=comp_id+"_"+str(ins.id)
			#ins.id=comp_id
			dummy_ins.comp_id=comp_id
			#ins.save()
			dummy_ins.save()
			
			roll_no=user.split("_")[1]
			try:
				attribute=student.objects.get(roll=roll_no)
				email=attribute.email
				msg=" Thanks for register a complaint to E-Complaint Service. please enter this otp after the solution of your problem\n OTP :- "+str(new_otp)
				p = Process(target=send_mail_to, args=(str(email),msg))
				p.start()
				return HttpResponseRedirect('/profile/')
			except:
				form=complaintForm()
	else:
		form=complaintForm()
	return render(request,'complaint/services.html',{'form':form})
def check_otp(new_otp,user_name):
	if(request.method=='POST'):
		form=otp_form(request.POST)
		if(form.is_valid()):
			input_otp=form.cleaned_data['otp']
			try:
				otp_original=otp.objects.get(otp_number=input_otp)
			except:
				return False
	else:
		form=otp_form()
	return render(request,'complaint/otp.html',{'form',form})
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
def admin_home(request):
	return render(request,'complaint/admin_home.html',{})

def furniture_(request):
	furniture_comp=dummy.objects.filter(Q(comp_type='Furniture') & Q(status='Registered'))
	furniture_comp_completed=dummy.objects.filter(Q(comp_type='Furniture') & Q(status='Completed'))
	return render(request,'complaint/furniture.html',{'furniture_comp':furniture_comp,'furniture_comp_completed':furniture_comp_completed})
def water_(request):
	water_comp=dummy.objects.filter(Q(comp_type='Water') & Q(status='Registered'))
	water_comp_completed=dummy.objects.filter(Q(comp_type='Water') & Q(status='Completed'))
	return render(request,'complaint/water_comp.html',{'furniture_comp':water_comp,'furniture_comp_completed':water_comp_completed})
def electricity_(request):
	electricity_comp=dummy.objects.filter(Q(comp_type='Electricity') & Q(status='Registered'))
	electricity_comp_completed=dummy.objects.filter(Q(comp_type='Electricity') & Q(status='Completed'))
	return render(request,'complaint/electricity_comp.html',{'furniture_comp':electricity_comp,'furniture_comp_completed':electricity_comp_completed})
def search(request):
	if(request.method=='POST'):
		form=search_form(request.POST)
		if(form.is_valid()):
			try:
				text=form.cleaned_data['complaint_id']
				print(text)
				atr=dummy.objects.get(comp_id=str(text))
				print(atr.status)
				return render(request,'complaint/search.html',{'form':form,'atr':atr})
			except:
				print("IN except")
				msg="!!NOT FOUND!!"
				return render(request,'complaint/search.html',{'form':form,'msg':msg})
			
	else:
		form=search_form()
	return render(request,'complaint/search.html',{'form':form})


