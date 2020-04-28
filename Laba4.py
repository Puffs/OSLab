import vk
import time

"""
Импортируем нужные библиотеки
"""

session = vk.Session(
    access_token='7a7216d948e6a6830000f451a09cb239b7a6ae8211aff137a3a7f292b963aafb321be98cbd012961912e6')

"""
Вставляем токен доступа созданного StandAlone приложения
"""

api = vk.API(session)
api = vk.API(session, v='5.92', lang='ru', timeout=10)

"""
Заходим под нашим именем
"""

api.wall.post(owner_id='189333279', message="Hello", v="5.92")

"""
Оставляем пост на стене с выбранным id  (Это мой id)

Так же экспериментально было установлено, что при задержке в 7 секунд вк не блокирует оставление записей капчей.
Можно оставлять на ночь и заспамливать чужие страницы)
"""

profiles = api.users.get(user_id=1)
print(profiles)

"""
Выводим пользователя с id=1 (Павла Дурова)
"""
