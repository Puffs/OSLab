import cv2 as cv
import time
"""
Импортируем нужные библиотеки
"""
def photo(a):
    """
 Создаем функцию для получения фотографии с камеры,
 принимающей на вход путь для сохранения фотографии (a)
    """
    cap = cv.VideoCapture(0)          # подключение к камере
    cap.read()
    ret, frame = cap.read()           # получение кадра с камеры
    time.sleep(2)                     # ожидание включения камеры
    cv.imwrite(a, frame)              # запись кадра
    cap.release()
    cv.destroyAllWindows()
    return()

def video(a):
    """
  Аналогичная функция для снятия видео
    """
    cap = cv.VideoCapture(0)
    video = cv.VideoWriter(a, -1, 20.0, (640, 480))    # создаем объект в который будет записываться видео
    while cap.isOpened():
        ret, frame = cap.read()      # получение изображения с камеры
        video.write(frame)           # запись кадра
        cv.imshow('Camera', frame)   # отображение изображения в окне
        if cv.waitKey(10) == 27:     # завершение записи по нажатию клавиши esc
            break
    video.release()
    cv.destroyAllWindows()
    return()

"""
Далее интерфейс для взаимодействия с пользователем.
В нем он может выбрать между снятием видео и фотографией
"""
while True:
    print('Выберите действие')
    name = str(input())
    if name == 'photo':
        photo(r'C:\Games\test\test.png')
    elif name == 'video':
        video(r'C:\Games\test\test.mp4')
    elif name == 'exit':
        exit(0)
    else:
        print('ошибка')
