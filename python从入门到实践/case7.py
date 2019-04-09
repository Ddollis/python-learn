class Restaurant(object):
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print 'restaurant_name' + self.restaurant_name
        print 'cuisine_type' + self.cuisine_type

    def open_restaurant(self):
        print self.restaurant_name + 'is opening'

    def set_number_served(self, number_served):
        self.number_served = number_served
        print 'the number of served:' + self.number_served

    def increment_number_served(self, number):
        self.number_served += number


class User(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print 'my name is ' + self.first_name + self.last_name

    def greet_user(self):
        print 'hello ' + self.first_name + self.last_name

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_icecream(self):
        print self.flavors


class Admin(User):
    def __init__(self, first_name, last_name):
        super(Admin, self).__init__(first_name, last_name)
        self.privileges = Privileges()


class Privileges(object):
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban users']):
        self.privileges = privileges

    def show_privileges(self):
        print self.privileges


user = User('qin', 'di')
user.increment_login_attempts()
print user.login_attempts
user.increment_login_attempts()
print user.login_attempts
user.reset_login_attempts()
print user.login_attempts
admin = Admin('qin', 'di')
admin.privileges.show_privileges()
