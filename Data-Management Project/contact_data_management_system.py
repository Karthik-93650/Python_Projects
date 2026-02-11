import csv
import os
import re

# Contact Data Management System using OOPS + CSV Persistence

class Contact:
    def __init__(self, name, mobileno, mailid):
        self.name = name
        self.mobileno = mobileno
        self.mailid = mailid


class AddContact:
    def add(self, phone):
        print("\n-> Adding Contact")

        name = input("Name: ").strip()

        if name in phone.contacts:
            print("Error: Contact already exists.")
            return

        mobile = input("Mobile No (10 digits): ").strip()
        if not mobile.isdigit() or len(mobile) != 10:
            print("Invalid mobile number.")
            return

        email = input("Email ID: ").strip()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email format.")
            return

        phone.contacts[name] = Contact(name, mobile, email)
        phone.save_to_csv()
        print("Contact added successfully.\n")


class UpdateContact:
    def update(self, phone):
        print("\n-> Update Contact")
        name = input("Enter name to update: ").strip()

        if name not in phone.contacts:
            print("Contact not found.")
            return

        contact = phone.contacts[name]
        print(f"Old Mobile: {contact.mobileno}")
        print(f"Old Email: {contact.mailid}")

        new_mobile = input("New Mobile (Enter to keep same): ").strip()
        if new_mobile:
            if not new_mobile.isdigit() or len(new_mobile) != 10:
                print("Invalid mobile number.")
                return
            contact.mobileno = new_mobile

        new_email = input("New Email (Enter to keep same): ").strip()
        if new_email:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
                print("Invalid email format.")
                return
            contact.mailid = new_email

        phone.save_to_csv()
        print("Contact updated successfully.\n")


class ListContacts:
    def list(self, phone):
        print("\n-> Contact List")

        if not phone.contacts:
            print("No contacts found.\n")
            return

        print(f"{'Name':<20}{'Mobile':<15}{'Email'}")
        print("-" * 50)

        for c in phone.contacts.values():
            print(f"{c.name:<20}{c.mobileno:<15}{c.mailid}")
        print()


class DeleteContact:
    def delete(self, phone):
        print("\n-> Delete Contact")
        name = input("Enter name to delete: ").strip()

        if name in phone.contacts:
            del phone.contacts[name]
            phone.save_to_csv()
            print("Contact deleted successfully.\n")
        else:
            print("Contact not found.\n")


class ExitApp:
    def exit(self):
        print("\nExiting application...")
        print("Data saved in contacts.csv (Excel compatible)")


class Phone:
    def __init__(self):
        self.contacts = {}
        self.filename = "contacts.csv"

        self.add_obj = AddContact()
        self.update_obj = UpdateContact()
        self.list_obj = ListContacts()
        self.delete_obj = DeleteContact()
        self.exit_obj = ExitApp()

        self.load_from_csv()

    def load_from_csv(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.contacts[row["Name"]] = Contact(
                    row["Name"], row["Mobile"], row["Email"]
                )

    def save_to_csv(self):
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Mobile", "Email"])
            writer.writeheader()
            for c in self.contacts.values():
                writer.writerow({
                    "Name": c.name,
                    "Mobile": c.mobileno,
                    "Email": c.mailid
                })

    def menu(self):
        while True:
            print("1. Add Contact")
            print("2. Update Contact")
            print("3. List Contacts")
            print("4. Delete Contact")
            print("5. Exit")

            try:
                choice = int(input("Choice: "))
            except ValueError:
                print("Enter a valid number.")
                continue

            if choice == 1:
                self.add_obj.add(self)
            elif choice == 2:
                self.update_obj.update(self)
            elif choice == 3:
                self.list_obj.list(self)
            elif choice == 4:
                self.delete_obj.delete(self)
            elif choice == 5:
                self.exit_obj.exit()
                break
            else:
                print("Invalid choice.\n")


if __name__ == "__main__":
    app = Phone()
    app.menu()
