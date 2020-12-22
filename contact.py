class Contact:

    def __init__(self, first_name, last_name, nickname=None, phone_number=None, email= None):
        self.id = id(self)
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.phone_number = phone_number
        self.email = email
        self.favorite = False
        self.work = False
        self.family = False
        self.freind = False


    def add_phone_num(self,phone_number):
        self.phone_number=phone_number

    def add_email(self,email):
        self.email= email

    def add_favorite(self,favorite):
        self.favorite= favorite

    def add_work(self,work):
        self.work= work

    def add_family(self,family):
        self.family= family

    def add_friend(self,friend):
        self.freind= friend    

    def add_nickname(self,nickname):
        self.nickname = nickname    