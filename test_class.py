# -*- coding: UTF-8 -*-

from my_library import models

profile = models.Profile('Diegues', '41999617816', 'Wipro')
print profile.name
profile.do_like()
print profile.get_like()
profile.do_like()
profile.print_data()

profile2 = models.ProfileVip('Fulano', 'Not available', 'MC', 'ful')
print profile2.phone
profile2.do_like()
profile2.print_data()
print profile2.get_credits()

print type(profile)
print profile.__class__


date = models.Date(2020, 07, 25)
date.print_data()

person = models.Person("Diegues Roveda", 75, 1.75)
person.print_imc()

person2 = models.Person("Gisele", 100, 1.69)
person2.print_imc()

profiles = models.Profile.generate_profile('profile_data.csv')

for prof in profiles:
    prof.print_data()

file = open('profile_data2.csv', 'w')
file.write('Pedro Gomes, 234454, Gomes e Amigos LTDA\n')
file.close()


#error
try:
    p2 = models.Profile('aa', '434343', 'abc')
except models.ArgumentInvalidError as error:
    print error