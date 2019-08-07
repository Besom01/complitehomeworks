import random
x = random.randint(1,100)
y = int(input('Kakot chislo ya zagadal?'))
while y != x:
    if y > x:
        print('menshe')
        y = int(input('Kakot chislo ya zagadal?'))
        if x == y:
            print('pravilno')
    elif y < x:
        print('bolshe')
        y = int(input('Kakot chislo ya zagadal?'))
        if x == y:
            print('pravilno')