from django.db import models

# Create your models here.
GENDER_CHOICE=(
				("Male","Male"),
				("Female","Female"),
			)
complaint_type=(("Furniture","Furniture"),
				("Electricity","Electricity"),
				("Water","Water"),
			)
status_choices=(
				("Registered","Registered"),
				("Seen","Seen"),
				("Assigned","Assigned"),
				("Completed","Completed"),
			)
class dummy(models.Model):
	comp_id=models.CharField(primary_key=True,max_length=20,default="16CA6000_0")
	comp_type=models.CharField(max_length=15,choices=complaint_type)
	date_time=models.DateTimeField(auto_now_add=True)
	hall=models.IntegerField(blank=False)
	room=models.DecimalField(max_digits=3,decimal_places=0,blank=False)
	mobile=models.DecimalField(max_digits=11,decimal_places=0,blank=False)
	comment=models.CharField(max_length=300)

class student(models.Model):
	roll=models.CharField(max_length=8,primary_key=True,blank=False)
	name=models.CharField(max_length=50,blank=False)
	hall=models.IntegerField(blank=False)
	gender=models.CharField(max_length=6,choices=GENDER_CHOICE)
	room=models.IntegerField(blank=False)
	mobile=models.CharField(max_length=10,blank=False)
	email=models.EmailField(unique=True,blank=False)
	password=models.CharField(max_length=20,blank=False)
class st_16CA6001(models.Model):
	date_time=models.DateTimeField(auto_now_add=True)
	comp_type=models.CharField(max_length=10,choices=complaint_type)
<<<<<<< HEAD
	status=models.CharField(max_length=10,default="Registered",choices=status_choices)

class st_16CA6023(models.Model):
	date_time=models.DateTimeField(auto_now_add=True)
	comp_type=models.CharField(max_length=10,choices=complaint_type)
	status=models.CharField(max_length=10,choices=status_choices,default='Registered')
	hall=models.IntegerField(blank=False)
	room=models.DecimalField(max_digits=3,decimal_places=0,blank=False)
	mobile=models.DecimalField(max_digits=10,decimal_places=0,blank=False)
	comment=models.CharField(max_length=300)

class st_16CA6004(models.Model):
	date_time=models.DateTimeField(auto_now_add=True)
	comp_type=models.CharField(max_length=10,choices=complaint_type)
	status=models.CharField(max_length=10,choices=status_choices,default='Registered')
	hall=models.IntegerField(blank=False)
	room=models.DecimalField(max_digits=3,decimal_places=0,blank=False)
	mobile=models.DecimalField(max_digits=10,decimal_places=0,blank=False)
	comment=models.CharField(max_length=300)
=======
	status=models.CharField(max_length=10,default="Registered")


class st_16CA6032(models.Model):
	date_time=models.DateTimeField(auto_now_add=True)
	comp_type=models.CharField(max_length=10,choices=complaint_type)
	status=models.CharField(max_length=10,default="Registered")



class st_16CA6023(models.Model):
	date_time=models.DateTimeField(auto_now_add=True)
	comp_type=models.CharField(max_length=10,choices=complaint_type)
	status=models.CharField(max_length=15)
>>>>>>> a0fe0a32e2a74f2620ad8b6eb8590cf79b89fbf2
