from django.db import models

# Create your models here.
GENDER_CHOICE=(
				("Male","Male"),
				("Female","Female"),
			)
class student(models.Model):
	roll=models.CharField(max_length=8,primary_key=True,blank=False)
	name=models.CharField(max_length=50,blank=False)
	hall=models.IntegerField(blank=False)
	gender=models.CharField(max_length=6,choices=GENDER_CHOICE)
	room=models.IntegerField(blank=False)
	mobile=models.CharField(max_length=10,blank=False)
	email=models.EmailField(unique=True,blank=False)
	password=models.CharField(max_length=20,blank=False)