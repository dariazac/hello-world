def fizzbuzz():
    for i in xrange(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print ("FizzBuzz")
        elif i % 3 == 0:
            print ("Fizz")
        elif i % 5 == 0:
            print ("Buzz")
        else:
            print (i)


fizzbuzz()


def fibsequ():
    a, b = 0, 1
    for i in xrange(0, 10):
        print a
        a, b = b, a + b


fibsequ()


def fibgen(num):
    a, b = 0, 1
    for i in xrange(0, num):
        yield "{}: {}".format(i + 1, a)
        a, b = b, a + b


for item in fibgen(10):
    print item
