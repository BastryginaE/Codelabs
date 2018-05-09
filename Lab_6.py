from math import sin, log, pi

# Создаем массив результатов
class Results:
    ResG = []
    ResF = []
    ResY = []

    def add_G(self, res):
        self.ResG.append(res)

    def add_F(self, res):
        self.ResF.append(res)

    def add_Y(self, res):
        self.ResY.append(res)

    def allresults(self):
        print('G: \n' +str(self.ResG))
        print('F: \n' +str(self.ResF))
        print('Y: \n' +str(self.ResY))

a = float(input('Enter a: '))
xMax = float(input('Enter maximum value for x: '))
xMin = float(input('Enter minimum value for x: '))
step_quantity = int(input('Enter the quantity of steps: '))
step = int(input('Enter the step value: '))

results = Results()

while xMin >= xMax:
    print('Максимальное значение X не может быть >= максимальному. Введите верные значения.')
    xMax = float(input('Enter maximum value for x: '))
    xMin = float(input('Enter minimum value for x: '))
x = xMin

# функция проверки данных, расчета и вывода на экран

def calc(a, x):

        try:
            G = -(8 * (7 * a ** 2 + 34 * a * x - 5 * x ** 2) / (27 * a ** 2 + 33 * a * x + 10 * x ** 2))
            results.add_G(G)
        except ValueError:
            print('Введите верное значение')
        try:
            F = -(1/(sin(72 * a**2 - 5 * a * x - 12 * x**2 - pi/2)))
            results.add_F(F)
        except ValueError:
            print('Введите верное значение')
        try:
            Y = log(42 * a**2 + 53 * a * x + 15 * x**2 + 1)
            results.add_Y(Y)
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

print(results.allresults())

