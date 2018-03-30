from smtplib import *
import smtplib
def send_mail_to(rcpt,msg):
	server = smtplib.SMTP()
	print ("Defined server")
	server.connect("smtp.gmail.com",587) # connecting to gmail smtp server .
	print ("Connected")
	server.ehlo()	
	server.starttls()	#Starting tls security 
	server.ehlo()	
	server.login("e.complaint.NIT@gmail.com",'123@qwerty') #will login to account
	print ("Logined")
	server.sendmail('e.complaint.NIT@gmail.com',rcpt,msg) # will send to message
	print("Sent")
	server.quit()