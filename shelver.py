import shelve


def get_dishes(filename, key='dishes'):
    with shelve.open(filename) as storage:
        try:
            dishes = storage[key]
        except KeyError:
            raise KeyError('Ошибка использования утилиты!\nНачните с команды `weeklymenu`')  # FIXME

        return dishes


def update_dishes(filename, dishes, key='dishes'):
    with shelve.open(filename) as storage:
        try:
            dishes = storage[key]
        except KeyError:  # П-ль начал работу с утилитой
            storage[key] = dishes
        else:  # П-ль нажал 3-ю команду, не завершив работу по сценарию
            updated_dishes = list()
            storage[key] = updated_dishes


def delete_dishes(filename, key='dishes'):
    with shelve.open(filename) as storage:
        del storage[key]
