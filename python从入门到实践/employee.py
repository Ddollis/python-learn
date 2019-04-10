class Employee(object):
    def __init__(self, first_name, last_name, salay):
        self.first_name = first_name
        self.last_name = last_name
        self.salay = salay

    def give_raise(self, add=5000):
        self.salay += add
