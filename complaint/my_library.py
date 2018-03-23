import os
from multiprocessing import Process
def create_instance(user):
	file=open('reduced/models.py','a+')
	file.write("\nclass "+str(user)+"(models.Model):\n")
	file.write("	to_acc=models.CharField(max_length=120)\n")
	file.write("	time=models.DateTimeField(auto_now_add=True)\n")
	file.write("	amount=models.DecimalField(default=0,max_digits=25,decimal_places=3)\n")
	file.close()
	#call_command('makemigrations')
def register_database(table_name):
	file=open('reduced/admin.py','a+')
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
