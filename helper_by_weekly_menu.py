from typing import List, Dict

from tabulate import tabulate

from break_line_by_particular_length import break_line_by_particular_length
import config
from utils import get_dishes_from


def get_weekmenu(dishes: List[Dict],
                 categories_names=config.CATEGORIES_NAMES,
                 days_of_week=config.DAYS_OF_WEEK,
                 tablefmt='grid'):

    """Формирует меню на неделю.

    Кол-во блюд на день, соответствует кол-ву категорий

    """

    dishes_names_per_day, dishes_names_per_week = None or [], None or []

    # List[Dict] -> 2 objects: List[List[str, str, str]]
    for idx, dish in enumerate(dishes, 1):
        dish_name = dish['title']
        dish_name_fitted_by_cell_size = break_line_by_particular_length(dish_name)
        if idx % len(categories_names) != 0:  # блюда НЕ объединены в меню на день
            dishes_names_per_day.append(dish_name_fitted_by_cell_size)
        else:
            dishes_names_per_day.append(dish_name_fitted_by_cell_size)
            dishes_names_per_week.append(dishes_names_per_day)
            dishes_names_per_day = []

    blank_table = dict(zip(days_of_week, dishes_names_per_week))
    weekmenu = tabulate(blank_table,
                        headers='keys',
                        showindex=categories_names,
                        tablefmt=tablefmt)

    return weekmenu


def main():

    dishes = get_dishes_from(config.FILENAME)

    weekmenu = get_weekmenu(dishes)

    print(weekmenu)


if __name__ == '__main__':
    main()
