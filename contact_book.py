class ContactBook:

    def __init__(self):
        self.contacts = dict()

    def add_contact(self,contact):
        self.contacts[contact.id]= contact

    def get_contact(self,id):
        print(self.contacts)
        return self.contacts.get(id)

    def remove_contact(self):
        pass

    def get_contacts(self):
        return self.contacts