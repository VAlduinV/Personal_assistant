from datetime import datetime, timedelta
import re
import pickle

file_name = 'AddressBook.bin'


def save(input, file_name):
    with open(file_name, 'wb') as file:
        pickle.dump(input.contacts, file)


def load(input, file_name):
    with open(file_name, 'rb') as file:
        input.contacts = pickle.load(file)
    return input.contacts


class Contact:
    def __init__(self, name, address, phone_number, email, birthday, notes=""):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.birthday = datetime.strptime(birthday, "%m/%d/%Y").date()
        self.notes = notes

    def __str__(self):
        return f"Name: {self.name}, Address: {self.address}, Phone number: {self.phone_number}, Email: {self.email}, Birthday: {self.birthday}, Notes: {self.notes}"

    def days_until_birthday(self):
        today = datetime.today().date()
        birthday = self.birthday.replace(year=today.year)
        if birthday < today:
            birthday = self.birthday.replace(year=today.year + 1)
        delta = birthday - today
        return delta.days


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def display_contacts(self):
        for contact in self.contacts:
            print(contact)
            print(f"Days until the next birthday: {contact.days_until_birthday()}")

    def display_contacts_for_input_days(self, days):
        print(f"Contacts with birthday in next {days} days:")
        count = 0
        for contact in self.contacts:
            next_birthday = contact.days_until_birthday()
            # print(f"Contacts with birthday in next {days} days")
            if next_birthday < days:
                count += 1
                print(contact)
        if count == 0:
            print(f"No contacts with birthday in next {days} days")


address_book = AddressBook()

try:
    load(address_book, file_name)
except:
    print("adress book is clean")

while True:
    print("\n--- Address Book Menu ---")
    print("1. Add/editing contact")
    print("2. Remove contact")
    print("3. Search for contact")
    print("4. Display all contacts")
    print("5. Display all contacts with birthday in next N days:")
    print("6. Quit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter name: ")
        address = input("Enter address: ")

        # Phone validation
        phone_result = False
        while not phone_result:
            phone_number = input("Enter phone number (only digits): ")
            if phone_number.isdigit():
                phone_result = True
            else:
                print("Wrong phone.")

        # Email validation
        email_result = False
        while not email_result:
            email = input("Enter email: ")
            if re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email):
                email_result = True
            else:
                print("Wrong email.")

        # Birthday validation
        birthday_result = False
        while not birthday_result:
            birthday = input("Enter birthday (MM/DD/YYYY): ")
            if datetime.strptime(birthday, "%m/%d/%Y"):
                birthday_result = True
            else:
                print("Wrong date.")

        notes = input("Enter notes: ")
        contact = Contact(name, address, phone_number, email, birthday, notes)
        address_book.add_contact(contact)
        print("Contact added.")

    elif choice == "2":
        name = input("Enter name to remove: ")
        address_book.remove_contact(name)
        print("Contact removed.")

    elif choice == "3":
        name = input("Enter name to search for: ")
        search_result = address_book.search_contact(name)
        if search_result:
            print(search_result)
            print(f"Days until the next birthday: {search_result.days_until_birthday()}")
        else:
            print("Contact not found.")

    elif choice == "4":
        address_book.display_contacts()

    elif choice == "5":
        days = int(input("Enter days: "))
        address_book.display_contacts_for_input_days(days)

    elif choice == "6":
        save(address_book, file_name)
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
