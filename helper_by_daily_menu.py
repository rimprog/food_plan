import random
from typing import Dict, List

from tabulate import tabulate

import config
from utils import get_dishes_from, \
                  get_renamed_column


def get_recipe_one_dish(dish: Dict,
                        cooking_steps_content=None,
                        column_names=('Приготовление блюда:', ),
                        tablefmt='rst'):

    cooking_steps_content = None or []
    dish_name = dish['data']['getRecipeById']['title']
    cooking_steps = dish['data']['getRecipeById']['recipeInstructions']

    for cooking_step in cooking_steps:
        cooking_step_content = cooking_step['title']
        cooking_steps_content.append(cooking_step_content)

    col_name = get_renamed_column(column_names, dish_name)
    blank_table = dict(zip([col_name], [cooking_steps_content]))
    cooking_steps_nums = range(1, len(cooking_steps) + 1)
    daymenu_one_dish = tabulate(blank_table, headers='keys',
                                showindex=cooking_steps_nums,
                                tablefmt=tablefmt)

    return daymenu_one_dish


def get_recipes(for_dishes: List[Dict], for_days=1, with_dishes_in_day=3) -> List[str]:

    recipes = None or []
    dishes_nums = for_days * with_dishes_in_day
    # Блюда, составляющие меню
    dishes_for_menu = random.sample(for_dishes, dishes_nums)

    left_bound, right_bound = 0, with_dishes_in_day
    for day in range(for_days):
        # Запоминать, какие блюда уже распределили по предыдущим дням
        dishes_per_day = dishes_for_menu[left_bound:right_bound]
        for dish in dishes_per_day:
            daymenu_one_dish = get_recipe_one_dish(dish)
            recipes.append(daymenu_one_dish)
        left_bound, right_bound = right_bound, right_bound + with_dishes_in_day

    return recipes


def main():
    dishes = get_dishes_from(config.FILENAME)

    recipes = get_recipes(dishes)

    print(*recipes)


if __name__ == '__main__':
    main()
