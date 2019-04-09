# with open('pi_digits.txt') as file_object:
#     """
#     contents = file_object.read()
#     print contents.rstrip()
#     """
#     # for line in file_object:
#     #     print line.rstrip()
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# print pi_string
# print len(pi_string)
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
print pi_string[:52] + '...'
print len(pi_string)
birthday = raw_input("enter your birthday:")
if birthday in pi_string:
    print 'your birthday in the pi'
else:
    print 'no'
