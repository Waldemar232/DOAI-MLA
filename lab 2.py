import math as m
b = True
a = 0
x, y = float(input('x=')), float(input('y='))
hp1 = x > y
hp2 = x < y
hp3 = x == y

def fx1(y):
    return m.sin(y - 0.5 * x)

def fx2(y):
    return m.exp^y

def fx3(x):
    return m.log(x)

while b:
    gh = input('f1 == 1, f2 == 2, f3 == 3: ')
    if gh == '1':
        a = fx1(y)
        b = False
    elif gh == '2':
        a = fx2(y)
        b = False
    elif gh == '3':
        a = fx3(x)
        b = False
    else:
        print('Invalid input')
        gh = ''

if hp1:
    c = y * m.sqrt(a) + 3 * m.sin(x)
elif hp2:
    c = x * m.sqrt(a)
elif hp3:
    c = abs(a**1/3) + (x**3)/3
print('c=', c)
