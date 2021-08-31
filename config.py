from environs import Env


env = Env()
env.read_env()

CATEGORIES_NAMES = [
    'Завтрак',
    'Обед',
    'Ужин'
]

COMMANDS_NAMES = [
    'weeklymenu',
    'ingredient',
    'dailymenu',
    'randomdailymenu'
]

DAYS_OF_WEEK = [
    'Понедельник',
    'Вторник',
    'Среда',
    'Четверг',
    'Пятница',
    'Суббота',
    'Воскресенье'
]

DELIKATESKA_FILENAME = env('DISHES_DELIKATESKA_FILENAME')

SHELVE_FILENAME = 'dish'
