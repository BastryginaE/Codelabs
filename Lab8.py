import numpy as np
import matplotlib.pyplot as plt
import time

plt.axis('equal')

# определяем множество точек
Points = int(input('Enter how many points you want: '))
res = []

# Определяем центр и границы окружности
c_x = float(input('Enter x for the central point: '))
c_y = float(input('Enter y for the central point: '))
radius = int(input('Enter radius length: '))
res_y = []
res_x = []

for id in enumerate(range(Points)):
    x = np.random.random_integers(-50, 50, Points)
    y = np.random.random_integers(-50, 50, Points)
    np.append(x, y)
    plt.scatter(x, y, color='blue')
    
# Создаем графическое изображение окружности
plt.scatter(c_x, c_y, Points)
C = plt.Circle((c_x, c_y), radius, facecolor='none', edgecolor='red')
plt.gca().add_artist(C)
plt.show()

# Находим токи внутри окружности

def count():
    for id in x:
        id_x = (id - c_x)**2
        res_x.append(id_x)
    for id in y:
        id_y = (id - c_y)**2
        res_y.append(id_y)
    Res = list(map(lambda a, b: a + b, res_x, res_y))
    not_enter = 0
    enter = 0
    for id in Res:
        if id <= radius**2:
            not_enter +=1
        else:
            enter +=1
    print('Не входит', not_enter, 'Входит', enter)

# Определяем точки, принадлежащие окружности, и время на подсчет этих точек
count()
start = time.time()
T = []
N_res = set(res)
Length = len(N_res)
end = time.time()
T.append(end - start)
print('Total time is ', *T)

# Записываем результаты в файл
T = str(T)
file = open('Time.txt', 'w')
file.write(T)
file.close()
print('The time has been put into Time.txt')




