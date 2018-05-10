from math import sin, log, pi

# Создаем массив результатов
ResG = []
ResF = []
ResY = []
result = {'G': ResG, 'F': ResF, 'Y': ResY}

a = float(input('Enter a: '))
xMax = float(input('Enter maximum value for x: '))
xMin = float(input('Enter minimum value for x: '))
step_quantity = int(input('Enter the quantity of steps: '))
step = int(input('Enter the step value: '))

while xMin >= xMax:
    print('Максимальное значение X не может быть >= максимальному. Введите верные значения.')
    xMax = float(input('Enter maximum value for x: '))
    xMin = float(input('Enter minimum value for x: '))
x = xMin

# функция проверки данных, расчета и вывода на экран

def calc(a, x):

        try:
            G = -(8 * (7 * a ** 2 + 34 * a * x - 5 * x ** 2) / (27 * a ** 2 + 33 * a * x + 10 * x ** 2))
            result['G'].append(G)
        except ValueError:
            print('Введите верное значение')
        try:
            F = -(1/(sin(72 * a**2 - 5 * a * x - 12 * x**2 - pi/2)))
            result['F'].append(F)
        except ValueError:
            print('Введите верное значение')
        try:
            Y = log(42 * a**2 + 53 * a * x + 15 * x**2 + 1)
            result['Y'].append(Y)
        except ValueError:
            print('Введите верное значение')

numeral = 0
while numeral <= step_quantity:
    calc(a, x)
    x += step
    if x > xMax:
        print('Величина X не может превышать максимальное значение.')
        break
    numeral += 1

# Открываем файл для записи
with open('allres.txt', 'w') as file:
    for id, object in result.items():
        file.write('{} = {}\n' .format(id, object))

# Удаление данных из массива
result = {}

# Открываем файл для чтения
with open('allres.txt', 'r') as file:
    for ob in file.readlines():
        id, object = ob.strip().split('=')
        print(id, '=', object)
