#Rapido Application
#1-10->per km 5rs
#11-15->per km 7rs
#16-20->per km 8rs
#20-30->per km 10rs
#>30->No ride
'''n=int(input("Enter your distance to travel in km's:"))
rc=0
if n in range(1,11):
    rc=n*5
    print("Your Ride cost is",rc)
elif n in range(11,16):
    rc=10*5+(n-10)*7
    print("Your Ride cost is",rc)
elif n in range(16,21):
    rc=10*5+5*7+(n-15)*7
    print("Your Ride cost is",rc)
elif n in range(21,31):
    rc=10*5+5*7+5*8+(n-20)*10
    print("Your Ride cost is",rc)
else:
    print("Sorry mate!No ride for you fella")'''

#Using functions
'''while 1:
    dist=int(input("Enter your distance to travel in km's:"))
    rc=0
    def bill(dist):
        if dist in range(1,11):
            rc=dist*5
            print("Your travel cost is",rc)
        elif dist in range(11,16):
            rc=10*5+(dist-10)*7
            print("Your travel cost is",rc)
        elif dist in range(16,21):
            rc=10*5+5*7+(dist-15)*8
            print("Your travel cost is",rc)
        elif dist in range(21,31):
            rc=10*5+5*7+5*8+(dist-20)*10
            print("Your travel cost is",rc)
        else:
            print("Sorry! nO Ride fEllA")
    bill(dist)'''

#Task:Railway ticket price using functions
#name=input("Enter your name please!")
'''gender=int(input("Enter your gender:1.)Male,2.)Female"))
age=int(input("Enter your age:"))
ticket=1000
def Male(age):
    if age>=60:
        ticket=ticket-30/100*ticket
        print("Your ticket price is",ticket)
    elif age<60:
        print("Your ticket price is",ticket)
def Female(age):
    if age>=60:
        ticket=ticket-70/100*ticket
        print("Your ticket price is",ticket)
    elif age<60:
        ticket=ticket-50/100*ticket
        print("Your ticket price is",ticket)
if gender==1:
    Male(age)
elif gender==2:
    Female(age)'''

'''name=input("Enter your name please!").title()
gender=int(input("Enter your gender:1.)Male,2.)Female"))
age=int(input("Enter your age:"))
ticket=1000
if gender==1:
    if age>=60:
        c=(70/100)*ticket
        print(f"{name}'s Ticket price is {c}")
    elif age<60:
        c=ticket
        print(f"{name}'s Ticket price is {c}")
elif gender==2:
    if age>=60:
        c=(30/100)*ticket
        print(f"{name}'s Ticket price is {c}")
    elif age<60:
        c=(50/100)*ticket
        print(f"{name}'s Ticket price is {c}")
else:
    print("Sorry ticket is Not Avaialable")'''

#Back Account 
account="c123"
password=9347
Balance=100000
while True:
    a=input("Please insert Your card")
    if a==account:
        print("Welcome Karthik")
        pin=int(input('Pin number'))
        if pin==password:
                b=int(input("choose options:/n,1.)Balance inquiry/n,2.)Withdrawl"))
                if b==1:
                    print(f"Your ACC BAL:{Balance}")
                elif b==2:
                    wd=int(input("enter the Amount to withdraw"))
                    if wd<=Balance:
                        updated=Balance-wd
                        print("Please collect the cash")
                        print(f"remaining balance:{updated}")
                        Balance=updated
                    else:
                        print("Insuffient balance")
                else:
                    print("Choose another option")
                    
        else:
            print("Incorrect password")
    else:
        print("Card Denied")
        


            



        



