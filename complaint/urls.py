from django.urls import path,include
from . import views

urlpatterns=[
	path('',views.home,name='home'),
	path('profile/',views.profile,name='profile'),
	path('contact/',views.contact,name='contact'),
	path('log/',views.log,name='log'),
	path('register/',views.register,name='register'),
	
]