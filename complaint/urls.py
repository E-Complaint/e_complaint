from django.urls import path,include
from . import views

urlpatterns=[
	path('',views.home,name='home'),
	path('profile/',views.profile,name='profile'),
	path('contact/',views.contact,name='contact'),
	path('log/',views.login,name='log'),
	path('register/',views.register,name='register'),
	path('signup/',views.signup,name='signup'),
	path('logout/',views.logout,name='logout'),	
	path('admin_login/',views.admin_login,name='admin_login'),
	path('admin_profile/',views.admin_profile,name='admin_profile'),
	path('furniture_com_detil/',views.furniture_,name='furniture_comp'),
	path('admin_login/',views.admin_login,name='admin_logout'),
	path('admin_home/',views.admin_home,name='admin_home'),
]
