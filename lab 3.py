import math as m
# Ввести свои данные
x1 = 1
xn = 6
step_x = 0.2
a = 3.9
b = 2.3


def fx(x):
    return (b * m.cos(x))/(1 + a**2 * m.sin(x)**3)


n = x1
while not n > xn:
    n += step_x
    print('x= ', round(n, 3), 'f(x) = ', round(fx(n), 7))
