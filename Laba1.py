import os

def readfile(l, a):
    """
    Функция записывает максимальные значения второго столбца каждого файла в массив
    Принимает на вход список названий файлов в директории (l)
    и пустой массив для записи значений (a)
    """

    b = []
    second = []
    line2 = []
    for j in f:
        way = path + '\\' + j                          # путь к файлу
        file = open(way, mode='r', encoding='latin_1') # открытие файла на чтение
        line = file.read().split(' ')                  # читаем файл и делим его на список по пробелу
        for i in line:                                 # убираем из списка пустые строки, переписываем в другой список
            if i != '':
                line2.append(i)
            else:
                pass
        for i in line2:           # приводим числа к стандартному виду, записываем их в массив, конвертируя во float
            i = i.replace('D', 'e')
            b.append(float(i))
        length = len(b)
        for i in range(1, length, 5):      # проходим по второму столбцу
            second.append(float(b[i]))
        a.append(max(second))              # записываем максимальное значение в массив
        line2.clear()                      # чистим вспомогательные массивы, закрываем файл
        b.clear()
        second.clear()
        file.close()


def writeresult(l, a):
    """
    Функция записывает максимальные значения второго столбца в файл
    Принимает на вход список названий файла в директории
    и массив с максимальными значениями второго столбца каждого файла
    """
    file = open(r"c:\Games\test\result.txt", mode='w', encoding='latin_1')
    k = 0
    for i in a:
        file.write(str(l[k]) + ':  ' + str(i) + '\n')
        k += 1
    file.close()


path = r"C:\Games\test\test"
f = os.listdir(path)  # получает список файлов в выбранной директории
maxsec = []           # также создаем массив для хранения максимального значения из второго столбца файла
readfile(f, maxsec)
writeresult(f, maxsec)


