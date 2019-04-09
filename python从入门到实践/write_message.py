filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('i love ning.\n')
    file_object.write('lvlvlv\n')

with open(filename, 'a') as file_object:
    file_object.write('123123\n')
    file_object.write('232323\n')
name = raw_input('input your name:')
with open(filename, 'a') as file_object:
    file_object.write(name)

while True:
    res = raw_input("why you don't like programming?")
    with open(filename, 'a') as file:
        file.write(res + '\n')
