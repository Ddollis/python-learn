alien_color = 'green'
if alien_color == 'green':
    print 'get five points'
elif alien_color == 'yellow':
    print 'get ten points'
elif alien_color == 'red':
    print 'get 15 points'

list1 = ['admin', 'aaa', 'bbb', 'ccc', 'ddd']
if list1:
    for i in list1:
        if i == 'admin':
            print 'hello ' + i + 'you are admin'
        else:
            print 'hello' + i + 'you are nomal'
else:
    print 'null'

current_users = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
new_users = ['DDD', 'eee', 'fff', 'ggg', 'hhh']

for i in new_users:
    i = i.lower()
    if i in current_users:
        print 'username has been used'
    else:
        print 'hello' + i

list1 = list(range(1, 10))
print list1
for i in list1:
    if i == 1:
        print '1st'
    elif i == 2:
        print '2nd'
    elif i == 3:
        print '3rd'
    else:
        print str(i) + 'th'
