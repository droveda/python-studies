# -*- coding: UTF-8 -*-
import re

from my_library import my_functions

print "\n\n--------------------"
print "---------common variables-----------"
print "--------------------\n"

salary = 7500.5j

salary2 = 6500.1

name = "Diegues Girotto Roveda"
address = 'Rua Marques do Parana'

name2 = name[0:7]
age = 39

print name2
print salary
print 'Invite of %s, %s years old' % (name, age)

print "\n\n--------------------"
print "---------LIST-----------"
print "--------------------\n"

invites = ['Fulano 1', 'Fulano 2', 'Fulano 3']

print invites[0]
print invites[1]
print invites[2]

print invites[0:2]
print invites[1:]

invites.append('Fulano 4')
print invites

invites.append(10)
print invites

invites.remove(10)
print invites

invites.remove('Fulano 3')
print invites

print "\n\n--------------------"
print "---------TUPLES AND DICTIONARY-----------"
print "--------------------\n"

invitation_types = ('vip', 'regular', 'half price', 'free')
print invitation_types
print invitation_types[2]
print invitation_types[1:]

prices = (50, 10, 20, 100, 200, 5, 3)
print "Min value in prices: %s" % min(prices)
print "Sum of prices is: %s" % sum(prices)
print "Max value in prices: %s" % max(prices)
print "Ordering the values of prices: %s" % sorted(prices)

invitation_types_dictionary = {'vip': 60, 'regular': 40, 'half_price': 30, 'free': 0}
print invitation_types_dictionary
print invitation_types_dictionary['half_price']
print invitation_types_dictionary.keys()
print invitation_types_dictionary.values()
print type(invitation_types_dictionary)

print "\n\n--------------------"
print "---------Functions-----------"
print "--------------------\n"

print my_functions.build_name(name);
print my_functions.build_name(address);
print my_functions.build_name('Alguma Coisa');
my_functions.send_invitation(name)
my_functions.proccess_invitation(name)

print "\n\n--------------------"
print "---------Getting value from the keyboard and regular expressions-----------"
print "--------------------\n"

results = re.findall('[A-Za-z]y[A-Za-z]+', 'Python or jython or Pypy')
results2 = re.findall('\\wy\\w+', 'Python3 or jython2 or Pypy')
results3 = re.findall('\\wy\\w+\d', 'Python3 or jython2 or Pypy')
results4 = re.findall('[A-Za-z]+\\d?', 'Python3 or jython2 or Pypy44')
print results
print results2
print results3
print results4

results5 = re.findall(r'[fF]\w{6,20}', 'Nico Flavio Fabiana Flaviana Romulo');
print results5

result = re.match(r'^#', '#Comantarios comecam com #!!!');
print result.group()

result2 = re.match(r'.*br$', 'http://www.google.com.br');
print result2.group()

def menu():
    names = []
    choice = ''
    while choice != '0':
        print 'Please choose 1 for store, 2 for remove, 3 for list names, 4 for alter name, 5 to search names or 0 to ' \
              'finish the app '
        choice = raw_input()
        if choice == '1':
            my_functions.store(names)
        elif choice == '2':
            my_functions.remove(names)
        elif choice == '3':
            my_functions.list_names(names)
        elif choice == '4':
            my_functions.update_name(names)
        elif choice == '5':
            my_functions.search_name(names)


#menu()
