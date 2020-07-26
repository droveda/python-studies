import re


def build_name(name):
    size = len(name)
    part1 = name[0:4]
    part2 = name[size - 4:size]
    return part1 + ' ' + part2


def send_invitation(name):
    print 'Sending invitation to %s' % build_name(name)


def proccess_invitation(name):
    print 'Processing invitation for %s' % (build_name(name))


def store(names):
    print 'Type the name'
    name = raw_input()
    names.append(name)


def remove(names):
    print 'Which name would you like to remove?'
    name = raw_input()
    names.remove(name)


def update_name(names):
    print 'Which name would you like to replace?'
    name = raw_input()
    if name in names:
        print 'Please inform the new value?'
        new_name = raw_input();
        index = names.index(name);
        names[index] = new_name
    else:
        print 'Name not found'


def search_name(names):
    print 'Please inform the name to search'
    name = raw_input()
    if name in names:
        print 'The name %s was found on index %s' % (name, names.index(name))
    else:
        print 'Name not found'


def regex_search(names):
    print('Type the regular expression')
    regex = raw_input()
    join_names = ' '.join(names)
    results = re.findall(regex, join_names)
    print(results)


def list_names(names):
    print names
