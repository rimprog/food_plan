from typing import Dict, List

from tabulate import tabulate

from break_line_by_particular_length import break_line_by_particular_length
import config
from utils import get_dishes_from, \
                  get_renamed_column


def get_recipe_one_dish(dish: Dict,
                        column_names=('Приготовление блюда:', ),
                        tablefmt='grid'):

    cooking_steps_content = None or []
    dish_name = dish['title']
    cooking_steps = dish['instructions']

    for cooking_step in cooking_steps:
        cooking_step_content = cooking_step['description']
        cooking_step_fitted_by_cell_size = break_line_by_particular_length(cooking_step_content,
                                                                           max_letters_before_break=100)
        cooking_steps_content.append(cooking_step_fitted_by_cell_size)

    col_name = get_renamed_column(column_names, dish_name)
    blank_table = dict(zip([col_name], [cooking_steps_content]))
    cooking_steps_nums = range(1, len(cooking_steps) + 1)
    daymenu_one_dish = tabulate(blank_table,
                                headers='keys',
                                showindex=cooking_steps_nums,
                                tablefmt=tablefmt)

    daymenu_one_dish_template = '{}\n'
    daymenu_one_dish_formatted = daymenu_one_dish_template.format(daymenu_one_dish)
    return daymenu_one_dish_formatted


def get_recipes(for_dishes: List[Dict],
                for_days=1,
                with_dishes_in_day=3) -> List[str]:

    recipes = None or []
    left_bound, right_bound = 0, with_dishes_in_day
    for day in range(for_days):
        # Запоминать, какие блюда уже распределили по предыдущим дням
        dishes_per_day = for_dishes[left_bound:right_bound]
        for dish in dishes_per_day:
            daymenu_one_dish = get_recipe_one_dish(dish)
            recipes.append(daymenu_one_dish)
        left_bound, right_bound = right_bound, right_bound + with_dishes_in_day

    return recipes


def main():
    dishes = get_dishes_from(config.DELIKATESKA_FILENAME)

    recipes = get_recipes(dishes, 2, 2)

    print(*recipes)


if __name__ == '__main__':
    main()
