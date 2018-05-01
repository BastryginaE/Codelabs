#Lab_2
from math import sin, log, pi

x = int(input('Enter x: '))
a = float(input('Enter a: '))
calculate = str(input('G функция G\nF функция F\nY функция Y\nEnter function: '))

if calculate == "G":
    try:
        G = -(8 * (7 * a ** 2 + 34 * a * x - 5 * x ** 2) / (27 * a ** 2 + 33 * a * x + 10 * x ** 2))
        print('G = ()' +str(G))
    except ValueError:
        print('Введите верное значение')

elif calculate == "F":
    try:
        F = -(1/(sin(72 * a**2 - 5 * a * x - 12 * x**2 - pi/2)))
        print('F = ()' +str(F))
    except ValueError:
        print('Введите верное значение')

elif calculate == "Y":
    try:
        Y = log(42 * a**2 + 53 * a * x + 15 * x**2 + 1)
        print('Y = ()' + str(Y))
    except ValueError:
        print('Введите верное значение')
else:
    print('Введите верное значение функции')
