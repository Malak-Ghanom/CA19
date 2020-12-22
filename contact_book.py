class ContactBook:

    def __init__(self):
        self.contacts = dict()

    def add_contact(self,contact):
        self.contacts[contact.id]= contact

    def get_contact(self,id):
        return self.contacts.get(id)

    def remove_contact(self,contact):
        self.contacts.pop(contact,None)

    def get_contacts(self):
        return self.contacts