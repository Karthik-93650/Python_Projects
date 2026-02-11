#Email Authentication/Automation
#OTP Genaration;
import random
import math
import smtplib #simple mail transfer protocal

digits = "$Karthik0123456789"
OTP = ""

for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]
msg = OTP + "  is your One Time Password"

s=smtplib.SMTP("smtp.gmail.com",587) #smtp.mail->source mail; 587->Port 587 used for/to transfer the otp to the mail
s.starttls() #used for/to protection of data(OTP)
s.login("tanuriumakarthik@gmail.com","pzmq hhhq npxh zxuc") #our mail id and the 16 digit app password

user = "tanuriumakarthik@gmail.com"
emailid=input("Enter The Email.id: ")
s.sendmail(user,emailid,msg)
while True:
    a=input("Enter your OTP: ")
    if a == OTP:
        print("Valid")
    else:
        print("Invalid")

