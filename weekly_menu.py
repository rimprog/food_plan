from tabulate import tabulate


def get_weekmenu(dishes_names, days_of_week, tablefmt):

    # List[str] -> List[List[str, str, str]]
    dish_name_template = '{dish_name}_{idx}'
    dishes_per_day, dishes_per_week = [], []
    for idx, _ in enumerate(days_of_week, 1):
        for dish_name in dishes_names:
            dish_fullname = dish_name_template.format(
                dish_name=dish_name,
                idx=idx
            )
            dishes_per_day.append(dish_fullname)
        dishes_per_week.append(dishes_per_day)
        dishes_per_day = []

    # -> Dict[str: List[str, str, str]]
    blank_table = dict(zip(days_of_week, dishes_per_week))

    weekmenu = tabulate(blank_table, headers='keys', tablefmt=tablefmt)

    return weekmenu


def main():

    # headers for the table
    days_of_week = [
        'Понедельник',
        'Вторник',
        'Среда',
        'Четверг',
        'Пятница',
        'Суббота',
        'Воскресенье'
    ]

    # content for the table
    dishes_names = [
        'breakfast dish',
        'dish for lunch',
        'dish for dinner'
    ]

    tablefmt = 'pretty'  # 'orgtbl'  # 'pretty'

    weekmenu = get_weekmenu(dishes_names, days_of_week, tablefmt)

    print(weekmenu)


if __name__ == '__main__':
    main()
