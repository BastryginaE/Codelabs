from math import sin, log, pi

a = float(input('Enter a: '))
xMax = float(input('Enter maximum value for x: '))
xMin = float(input('Enter minimum value for x: '))
step_quantity = int(input('Enter the quantity of steps: '))
step = int(input('Enter the step value: '))

# Создаем массивы

box1 = []
box2 = []

while xMin >= xMax:
    print('Максимальное значение X не может быть >= максимальному. Введите верные значения.')
    xMax = float(input('Enter maximum value for x: '))
    xMin = float(input('Enter minimum value for x: '))

calculate = str(input('G функция G\nF функция F\nY функция Y\nEnter function: '))
x = xMin

# функция проверки данных, расчета и вывода на экран

def calc(a, x):

    if calculate == "G":
        try:
            G = -(8 * (7 * a ** 2 + 34 * a * x - 5 * x ** 2) / (27 * a ** 2 + 33 * a * x + 10 * x ** 2))
            box1.append(x)
            box2.append(G)
        except ValueError:
            print('Введите верное значение')
    elif calculate == "F":
        try:
            box1.append(x)
            F = -(1/(sin(72 * a**2 - 5 * a * x - 12 * x**2 - pi/2)))
            box1.append(x)
            box2.append(F)
        except ValueError:
            print('Введите верное значение')

    elif calculate == "Y":
        try:
            Y = log(42 * a**2 + 53 * a * x + 15 * x**2 + 1)
            box1.append(x)
            box2.append(Y)
        except ValueError:
            print('Введите верное значение')
    else:
        print('Введите верное значение функции')
        pass

numeral = 0
while numeral <= step_quantity:
    calc(a, x)
    x += step
    if x > xMax:
        print('Величина X не может превышать максимальное значение.')
        break
    numeral += 1

# Выводим полученный массив в виде одной строки
print('Results: ', *box2)

# Задаем шаблон и находим соответствия
template = float(input('Enter what you would like to find: '))
print('There are: ', box2.count(template))
pass

# Считаем четные цифры в целом числе
template = int(input('Enter the number: '))
put = 0
while template > 0:
    if template % 2 == 0:
        put += 1
    print('Found: ', put)
    template = template // 10
else:
    print('0')












