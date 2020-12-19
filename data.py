from contact_book import ContactBook
from contact import Contact

def generate_contacts():
    #create a contact book
    contact_book= ContactBook ()

    contact = Contact("Malak","Ghanom")
    contact1 = Contact("Malik","saadi")
    contact2 = Contact("Esraa","Ghweri")
    contact3 = Contact("Alaa","Alahmad")
    
    #add contacts to contacts book
    contact_book.add_contact(contact)
    contact_book.add_contact(contact1)
    contact_book.add_contact(contact2)
    contact_book.add_contact(contact3)

    return contact_book