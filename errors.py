from my_library import models

file = None
try:
    file = open('not_exist.csv', 'r')
    print 'File opened'
    file.close()
except IOError as error:
    print 'File not found! %s' % error
finally:
    if file is not None:
        print 'Closing file'
        file.close()

