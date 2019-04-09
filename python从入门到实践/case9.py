try:
    num1 = int(raw_input("input number1:"))
    num2 = int(raw_input("input number2:"))
except ValueError:
    print 'mistake'
else:
    print "add:" + str(num1 + num2)
