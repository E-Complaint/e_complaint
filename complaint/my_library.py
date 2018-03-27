import os
from multiprocessing import Process
def create_instance(user):
	file=open('complaint/models.py','a+')
	file.write("\nclass "+str(user)+"(models.Model):\n")
	#file.write("	comp_id=models.CharField(max_length=120)\n")
	file.write("	date_time=models.DateTimeField(auto_now_add=True)\n")
	file.write("	comp_type=models.CharField(max_length=10,choices=complaint_type)\n")
	file.write("	status=models.CharField(max_length=10,choices=status_choices,default='Registered')\n")
	file.write("	hall=models.IntegerField(blank=False)\n")
	file.write("	room=models.DecimalField(max_digits=3,decimal_places=0,blank=False)\n")
	file.write("	mobile=models.DecimalField(max_digits=10,decimal_places=0,blank=False)\n")
	file.write("	comment=models.CharField(max_length=300)\n")
	file.close()
	#call_command('makemigrations')
def register_database(table_name):
	file=open('complaint/admin.py','a+')
	file.write("\nadmin.site.register("+str(table_name)+")\n")
	file.close()
	
def makemigrations(z):
	os.system("python3 manage.py makemigrations")
	os.system("python3 manage.py migrate")
def create_dynamic(table_name):
	create_instance(table_name)
	register_database(table_name)
	p = Process(target=makemigrations, args=('bob',))
	p.start()
