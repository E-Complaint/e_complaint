from django.urls import path,include
from . import views

urlpatterns=[
	path('',views.home,name='home'),
	path('blog/',views.blog,name='blog'),
	path('contact/',views.contact,name='contact'),
	path('portfolio/',views.portfolio,name='portfolio'),
	path('services/',views.services,name='services'),
	path('signup/',views.signup,name='signup'),
]