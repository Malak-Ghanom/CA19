from contact_book import ContactBook
from contact import Contact

def generate_contacts():
    #create a contact book
    contact_book= ContactBook ()

    contact = Contact("Ahmad","Abu-Alnadi","modi",int('07964313131'),'ahmad@gmail.com')
    contact0 = Contact("Malak","Ghanom","modi",int('07964313131'),'ahmad@gmail.com')
    contact1 = Contact("Malik","saadi","modi",int('07964313131'),'ahmad@gmail.com')
    contact2 = Contact("Esraa","Ghweri","modi",int('07964313131'),'ahmad@gmail.com')
    contact3 = Contact("Alaa","Alahmad","modi",int('07964313131'),'ahmad@gmail.com')
    
    #add contacts to contacts book
    contact_book.add_contact(contact)
    contact_book.add_contact(contact0)
    contact_book.add_contact(contact1)
    contact_book.add_contact(contact2)
    contact_book.add_contact(contact3)

    return contact_book