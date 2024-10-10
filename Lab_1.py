import math as m
x, y, z = float(input('x=')), float(input('y=')),float(input('z='))
a = y**m.sqrt(abs(x))
b = x - y/2
c = m.atan(z)
s = m.log(a) * b + m.sin(c) **2
print('s=', s)