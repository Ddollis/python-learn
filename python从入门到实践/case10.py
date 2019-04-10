import json

numbers = [2, 3, 4, 5, 6, 7, 11, 12]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print numbers
