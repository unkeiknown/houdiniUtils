class Employee:
    def __init__(self, first_name="", last_name="", age=0, role=""):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.role = role

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @full_name.setter
    def full_name(self, value):
        first, last = value.split()
        self.first_name = first
        self.last_name = last
    
    @full_name.deleter
    def full_name(self):
        del self.first_name

    @property
    def email(self):
        return self.first_name + "." + self.last_name + "@rebelway.comm"
    
    @email.setter
    def email(self, value):
        value1, value2 = value.split()
        return value1 + "." + value2 + "@rebelway.com"


















