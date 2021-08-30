import random
from typing import List, Dict

from tabulate import tabulate

import config
from utils import get_dishes_from, \
                  get_fitted_cell_size


def get_weekmenu(dishes: List[Dict],
                 dishes_names_per_day=None,
                 dishes_names_per_week=None,
                 categories_names=('Завтрак', 'Обед', 'Ужин', ),
                 tablefmt='grid'):

    days_of_week = config.DAYS_OF_WEEK
    dishes_names_per_day, dishes_names_per_week = None or [], None or []
    dishes_for_week = random.sample(dishes, 21)

    # List[Dict] -> 2 objects: List[List[str, str, str]]
    for idx, dish in enumerate(dishes_for_week, 1):
        dish_name = dish['data']['getRecipeById']['title']
        fitted_dish_name = get_fitted_cell_size(dish_name)
        if idx % len(categories_names) != 0:  # блюда НЕ объединены в меню на день
            dishes_names_per_day.append(fitted_dish_name)
        else:
            dishes_names_per_day.append(fitted_dish_name)
            dishes_names_per_week.append(dishes_names_per_day)
            dishes_names_per_day = []

    blank_table = dict(zip(days_of_week, dishes_names_per_week))
    weekmenu = tabulate(blank_table, headers='keys', tablefmt=tablefmt)

    return weekmenu


def main():

    dishes = get_dishes_from(config.FILENAME)

    weekmenu = get_weekmenu(dishes)

    print(weekmenu)


if __name__ == '__main__':
    main()
