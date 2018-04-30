# Lab_1
from math import sin, log, pi


x = float(input('Enter x: '))
a = float(input('Enter a: '))
G = -(8*(7 * a**2 + 34 * a * x - 5 * x**2)/(27 * a**2 + 33 * a * x + 10 * x**2))
F = -(1/(sin(72 * a**2 - 5 * a * x - 12 * x**2 - pi/2)))
Y = log(42 * a**2 + 53 * a * x + 15 * x**2 + 1)

print ('G = {}, F = {}, Y = {}'.format(G, F, Y))

# Lab_2
from math import sin, log, pi

x = int(input('Enter x: '))
a = float(input('Enter a: '))
G = -(8*(7 * a**2 + 34 * a * x - 5 * x**2)/(27 * a**2 + 33 * a * x + 10 * x**2))
F = -(1/(sin(72 * a**2 - 5 * a * x - 12 * x**2 - pi/2)))
Y = log(42 * a**2 + 53 * a * x + 15 * x**2 + 1)

calculate = str(input('Enter function: '))

if calculate == G:
    G = -(8 * (7 * a ** 2 + 34 * a * x - 5 * x ** 2) / (27 * a ** 2 + 33 * a * x + 10 * x ** 2))
    print ('G = {}'.format(G))

elif calculate != "G":
    print ('Введено неверное значение. Введите G.')




