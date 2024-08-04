import pickle

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def get_contact(self, name):
        return self.contacts.get(name, None)
    
    def list_contacts(self):
        return self.contacts.items()
    
    def __repr__(self):
        return f"AddressBook({self.contacts})"
    
def save_data(book, filename= "addressbook.pk1"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data (filename="addressbook.pk1"):
    try:
       with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
        
def main():

    book = load_data()

    while True:
        print("\n1. Add contact")
        print("\n2. Remove contact")
        print("\n3. Show contact")
        print("\n4. Show all contacts")
        print("\n5. Close")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input ("Enter phone number: ")
            book.add_contact(name, phone)
            print(f"Contact {name} with number {phone} added.")

        elif choice == "2":
            name = input("Enter contact name to remove")
            book.remove_contact(name)
            print(f"Contact {name} has been deleted.")

        elif choice == "3":
            name == input("Enter contact name for search: ")
            contact = book.get_contact(name)
            if contact:
               print(f"Contact {name}: {contact}")
            else:
                print(f"Contact {name} not found.")

        elif choice == "4":
            contacts = book.list_contacts()
            if contacts:
                for name, phone in contacts:
                    print(f"Name: {name}, Number: {phone}")
            else:
                print (f"No contacts")

        elif choice == "5":
            save_data(book)
            print(f"Data saved. Program exit.")
            break
            
        else:
            print("Not valid choice. Try again.")

if __name__ == "__main__":
    main()
    

    