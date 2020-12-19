

class Contact:

    def __init__(self, first_name, last_name):
        self.id = id(self)
        self.first_name = first_name
        self.last_name = last_name
        self.phone_numbers = []


    def add_phone_num(self,phone_number):
        self.phone_numbers.append(phone_number)

