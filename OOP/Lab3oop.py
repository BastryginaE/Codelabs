import argparse  #импортируем модуль для обработки агрументов командной строки

ar_poly = []  #создаем список, куда будут сохраняться аргументы, полученные из командной строки
res =[]  #создаем список, куда будут сохраняться результаты вычислений

class cl_parser:  #создаем класс для получения аргументов, которые пользователь ввёл в командную строку
    def __init__(self):  #создаем объект класса с параметрами, где х - это переменная, хранящая результаты
        # вычисления значения каждой составной части полинома.

        cl_parser = argparse.ArgumentParser()  #передаем созданному классу параметры класса ArgumentParser модуля argparse
        cl_parser.add_argument ('--poly', type=int, nargs='*') #производим добавление опций в созданный класс
        # при помощи метода add_argument, где '--poly' - имя опции (команды, которую выполняет метод (?), опциональный аргумент),
        # nargs='*' - ключ, указывающий, количество аргументов к опции (все аргументы помещаются в один список),

        vpoly = cl_parser.parse_args()  #считываем аргументы из командной строки с помощью метода parse_args
        #  и помещаем их в переменную

        for poly in vpoly.poly:  #создаем цикл, попорядку анализирующий значения, поступающие в переменную vpoly из класса
            ar_poly.append(int(poly)) # cl_parser, который собирает их из командной строки с помощью параметров,
            # переданных ему из класса ArgumentParser. Знак "." связывает переменную vpoly и опцию cl_parser.add_argument
            # посредством указания имени этой опции (poly), poly в выражении for poly означает каждый конкретный
            # аргумент, взятый из переменной vpoly для проверки и добавления в конец списка ar_poly; (int(poly)) - это
            # значение (всегда пишется в круглых скобках), которое добавляется в список, тип данных этого
            # значения - целочисленный.

        # создаем цикл для вычисления значений полинома
        i = 0 # переменная, в которую будут сохраняться вычисленные значения переменной х после каждой итерации цикла
        while i < len(ar_poly):  #проверка истинности выражения: количество элементов, присвоенных переменной i,
            # не превосходит длину списка  ar_poly
            x = 1/ar_poly[i]*3  # присваиваем переменной х вычисляемые в ходе итераций значения элементов полинома, i - это индекс элемента списка
            res.append(x)  #добавляем вычесленные значения в список результатов вычислений
            i+=1  #с каждой новой итерацией увеличиваем значение переменной i на 1 (по условию задачи)

            sum(res)  # функция, которая вычисляем сумму элементов полинома.

print(sum(res))



