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
        try:  # П-ль уже получил меню на неделю
            dishes = storage[key]
        except KeyError:  # П-ль начал работу с утилитой
            storage[key] = dishes


def delete_dishes(filename, key='dishes'):
    with shelve.open(filename) as storage:
        try:
            del storage[key]
        except KeyError:  # П-ль начал работу с утилитой
            pass
