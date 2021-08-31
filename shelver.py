import shelve


def get_dishes(filename, key='dishes'):
    with shelve.open(filename) as storage:
        try:
            dishes = storage[key]
        except KeyError:  # П-ль нарушил логику работы утилиты
            msg = 'Ошибка использования утилиты! Начните с команды `weeklymenu`'
            raise KeyError(msg)

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
