magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print magician

for value in range(1, 5):
    print value

numbers = list(range(1, 6))
print numbers
even_numbers = list(range(2, 11, 2))
print even_numbers

squares = [value ** 2 for value in range(1, 11)]
print squares

res = []
for i in range(1, 21):
    res.append(i)
print res
res = [i for i in range(1, 1000001)]
print max(res)
print min(res)
print sum(res)
res = [odd for odd in range(1, 21, 2)]
for i in res:
    print i
res = []
for i in range(3, 31):
    if i % 3 == 0:
        res.append(i)
print res
res = [i ** 3 for i in range(1, 11)];
print res
