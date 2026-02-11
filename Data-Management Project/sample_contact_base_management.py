#Contact base management system using OOPS;
'''1.)Add Contacts:(click 1 and then click 3 to view in list of contacts)
    name:
    mobile.no:
    mailid:
2.)Update contacts:(Press 2)
    contact:
3.)list of contacts:(Press 3)
    view no.of contacts added
4.)Delete contacts:(Press 4)
5.)Exit  (Press 5)'''

class Contact:
    def __init__(self,name,mobileno,mailid):
        self.name=name
        self.mobileno=mobileno
        self.mailid=mailid
        
class Addcontact():
    def add(self,phone):
        print("\n->Adding contacts")
        name=input("Name: ")
        mobileno=int(input("Mobile.no: "))
        mailid=input("Mail.id: ")
        
        phone.contacts[name] = Contact(name,mobileno,mailid)
        print("Contact Added Successfully\n")
        
class Updatecontact():
    def update(self,phone):
        print("\n->Updating Contacts")
        name=input("name: ")
        print("Old Mobile.no:",phone.contacts[name].mobileno)
        print("Old Mail.id:",phone.contacts[name].mailid)

        if name in phone.contacts:
            mobileno=int(input("New Mobile.No: "))
            mailid=input("New Mail.id: ")
            phone.contacts[name].mobileno = mobileno
            phone.contacts[name].mailid = mailid
            print("Contact Updated Successfully\n")
        else:
            print("Contact Not Found\n")
            
class List_contact():
    def list(self,phone):
        print("\n->List of contacts")

        if phone.contacts == { }:
            print("No Contacts Found\n")
            return

        for contact in phone.contacts.values(): #to get values in the phone.contacts dictionary we use .values
            print(f"Name: {contact.name}, Mobile.No: {contact.mobileno}, Mail.id: {contact.mailid}")
        print()

class Deletecontact():
    def delete(self,phone):
        print("\n->Delete Contact")
        name=input("Enter contact name to Delete: ")

        if name in phone.contacts:
            del phone.contacts[name]
            print("Contact Deleted!\n")
        else:
            print("Contact Not Found\n")

class Exit():
    def exit(self):
        print("\nExiting... Thanks for Choosing Contact Base Managemant System!")


class Phone():
    def __init__(self):
        self.contacts={ }

        self.obj1=Addcontact()
        self.obj2=Updatecontact()
        self.obj3=List_contact()
        self.obj4=Deletecontact()
        self.obj5=Exit()

    def menu(self):
        while 1:
            print("1. Add Contact")
            print("2. Update Contact")
            print("3. List Contacts")
            print("4. Delete Contact")
            print("5. Exit")

            choice = int(input("Choice: "))

            if choice == 1:
                self.obj1.add(self)
            elif choice == 2:
                self.obj2.update(self)
            elif choice == 3:
                self.obj3.list(self)
            elif choice == 4:
                self.obj4.delete(self)
            elif choice == 5:
                self.obj5.exit()
                break
            else:
                print("Invalid Choice!")

p=Phone()
p.menu()

            















    
    
