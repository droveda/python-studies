# -*- coding: UTF-8 -*-


class Profile(object):
    """Standard class for user profiles"""

    def __init__(self, name, phone, company):
        if len(name) < 3:
            raise ArgumentInvalidError('Name should be at least 3 characters')
        self.name = name
        self.phone = phone
        self.company = company
        self.__like = 0

    def print_data(self):
        print "Name: %s, Phone: %s, Company: %s, Likes: %s" % (self.name, self.phone, self.company, self.__like)

    def do_like(self):
        self.__like += 1

    def get_like(self):
        return self.__like

    @classmethod
    def generate_profile(clazz, file_name):
        file = open(file_name, 'r')
        profiles = []

        for line in file:
            values = line.split(',')
            profiles.append(clazz(*values))
        file.close()
        return profiles


class Date(object):

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def print_data(self):
        print '%s/%s/%s' % (self.day, self.month, self.year)


class Person(object):

    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def print_imc(self):
        print "IMC of %s is %s" % (self.name, self.calc_imc())

    def calc_imc(self):
        return self.weight / (self.height * self.height)


class ProfileVip(Profile):
    """Standard class for user profiles"""

    def __init__(self, name, phone, company, nickname=''):
        super(ProfileVip, self).__init__(name, phone, company)
        self.nickname= nickname

    def get_credits(self):
        return super(ProfileVip, self).get_like() * 10.0


class ArgumentInvalidError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)

