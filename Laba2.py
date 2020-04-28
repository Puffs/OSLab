import os
import matplotlib.pyplot as plt


def par(a, l):
    """
    Функция определяет коэффицент R
    Принимает на вход массив для хранения значений R
    и список названий файлов в директории
    """
    for i in l:
        i = i.replace('D', 'E').replace('.dat', ' ').replace('psi_G=', ' ').replace('psi2_G=',
                                                                                    ' ')  # Выделяем число из нахвания файла
        a.append(float(i))  # записываем значения параметра в массив
    return a


def readfile(l, a):
    """
     Функция записывает максимальные значения второго столбца в файл
    Принимает на вход список названий файла в директории
    и массив с максимальными значениями второго столбца каждого файла
    """
    b = []
    second = []
    line2 = []
    for j in f:
        way = path + '\\' + j  # путь к файлу
        file = open(way, mode='r', encoding='latin_1')  # открытие файла на чтение
        line = file.read().split(' ')  # читаем файл и делим его на список по пробелу
        for i in line:  # убираем из списка пустые строки, переписываем чиста в другой список
            if i != '':
                line2.append(i)
            else:
                pass
        for i in line2:  # приводим числа к стандартному виду, записываем их в массив, конвертируя во float
            i = i.replace('D', 'e')
            b.append(float(i))
        length = len(b)
        for i in range(1, length, 5):  # проходим по второму столбцу
            second.append(float(b[i]))
        a.append(max(second))  # записываем максимальное значение в массив
        line2.clear()  # чистим вспомогательные массивы, закрываем файл
        b.clear()
        second.clear()
        file.close()


def writeresult(l, a):
    """Функция для записи значений в файл

    :pararm l: список, содержащий название файлов
    :param a: список для записи максимального значения из второго столбца

    :return: список максимальных значений второго столбца
    """
    file = open(r"c:\pyt\result.txt", mode='w', encoding='latin_1')
    k = 0
    for i in a:
        file.write(str(l[k]) + ':  ' + str(i) + '\n')
        k += 1
    file.close()


path = r"C:\Games\test\test"
f = os.listdir(path)
c = []  # массив для хранения значений R
maxsec = []  # для хранения максимального значения из второго столбца файла
par(c, f)
readfile(f, maxsec)
print(f)
print(c)
print(maxsec)
plt.scatter(c, maxsec)
plt.show()