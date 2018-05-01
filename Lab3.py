from math import sin, log, pi

# границы изменения х
a = int(input('Enter a: '))
xMax = int(input('Enter maximum value for x: '))
xMin = int(input('Enter minimum value for x: '))
step_quantity = int(input('Enter the quantity of steps: '))
step = int(input('Enter the step value: '))

# цикл проверки значений Х
while xMin >= xMax:
    print('Максимальное значение X не может быть >= максимальному. Введите верные значения.')
    xMax = int(input('Enter maximum value for x: '))
    xMin = int(input('Enter minimum value for x: '))

calculate = str(input('G функция G\nF функция F\nY функция Y\nEnter function: '))
x = xMin

# функцция проверки данных, расчета и вывода на экран

def calc (a, x):

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

# цикл расчета с изменяющимся значением шага

figure = 0
while figure <= step_quantity:
    calc(a, x)
    x += step
    if x > xMax:
        print('Величина X не может превышать максимальное значение.')
        break
    figure += 1
