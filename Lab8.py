import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches
import matplotlib.path
import time

plt.axis('equal')

# определяем множество точек
Points = int(input('Enter how many points you want: '))
res = []

# Определяем центр и границы окружности
c_x = int(input('Enter x for the central point: '))
c_y = int(input('Enter y for the central point: '))
radius = int(input('Enter radius length: '))

for id in enumerate (range(Points)):
    x = np.random.random(-50, 50, Points)
    y = np.random.random(-50, 50, Points)
    np.append(x, y)
    plt.scatter(x, y, color = 'blue')

# Находим токи внутри окружности
    if ((c_x**2)+(c_y**2)) == radius**2:
        res.append(format([x, y]))
        print('This point is the center of the circle', (x, y))

    elif ((x - c_x)**2) + ((y - c_y)**2) == radius**2:
        res.append(format([x, y]))
        print('This point belongs to the circle', (x, y))

    elif ((x - c_x)**2) + ((y - c_y)**2) < radius**2:
        res.append(format([x, y]))
        print('This point is inside the circle', (x, y))

# Создаем графическое изображение окружности
def DrawCircle (axes):
    circ = matplotlib.patches.Circle(c_x, c_y, radius='', fill=False, color='g')
    axes.add_path(circ)
    plt.show()

# Определяем точки, принадлежащие окружности, и время на подсчет этих точек
start = time.time()
T = []
N_res = set(res)
print = ('The result:', N_res)
Length = len(N_res)
print('We found these points: ', Length)
end = time.time()
T.append(end - start)
print('Total time is ', *T)

# Записываем результаты в файл
T = str(T)
file = open('Time.txt', 'w')
file.write(T)
file.close()
print('The time has been put into Time.txt')



