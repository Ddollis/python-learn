alien_0 = {'color': 'green', 'points': 5}
print alien_0['color']
print alien_0["points"]
print alien_0

loved = {
    'first_name': 'wang',
    'last_name': 'ning',
    'age': 18,
    'city': 'wuhan'
}
print loved
for key, value in loved.items():
    print 'key:' + str(key)
    print 'value:' + str(value)

for key in loved.keys():
    print key