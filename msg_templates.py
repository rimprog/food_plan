from tabulate import tabulate


def main():

    # headers for the table
    days_of_week = (
        'Понедельник',
        'Вторник',
        'Среда',
        'Четверг',
        'Пятница',
        'Суббота',
        'Воскресенье'
    )

    # content for the table
    dishes = [[
        'breakfast dish',
        'dish for lunch',
        'dish for dinner'],
    ]

    tablefmt = 'pretty'  # 'orgtbl'  # 'pretty'
    table = tabulate(dishes, headers=days_of_week, tablefmt=tablefmt)

    print(table)


if __name__ == '__main__':
    main()
