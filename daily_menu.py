import random
from typing import Dict, List

from tabulate import tabulate

from ingredient import get_dish_from


def get_daymenu_one_dish(filename,
                         cooking_steps_content=None,
                         column_name=['Приготовление блюда:'],
                         tablefmt='rst'):

    cooking_steps_content = None or []

    dish = get_dish_from(filename)
    dish_name = dish['data']['getRecipeById']['title']
    cooking_steps = dish['data']['getRecipeById']['recipeInstructions']

    for cooking_step in cooking_steps:
        cooking_step_content = cooking_step['title']
        cooking_steps_content.append(cooking_step_content)

    column_name += [dish_name]
    col_name = ' '.join(column_name)

    blank_table = dict(zip([col_name], [cooking_steps_content]))
    daymenu_one_dish = tabulate(blank_table, headers='keys', showindex=True, tablefmt=tablefmt)

    return daymenu_one_dish


def main():
    filename = 'dish.json'

    daymenu = get_daymenu_one_dish(filename)

    print(daymenu)



if __name__ == '__main__':
    main()
