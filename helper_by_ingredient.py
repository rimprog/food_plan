import random
from typing import List, Dict

from tabulate import tabulate

import config
from utils import check_in, \
                  get_dishes_from, \
                  set_and_get_nominal_price


def get_ingredients(dishes: List[Dict],
                    column_names=('Ингредиент', 'Цена'),
                    tablefmt='grid'):

    ingregient_and_price = {}
    dishes_for_week = random.sample(dishes, 21)

    for dish in dishes_for_week:
        ingrs_per_dish = dish['data']['getRecipeById']['recipeIngredients']
        for ingredient in ingrs_per_dish:
            ingr_name = ingredient['title']
            # ингредиент уже есть в ingregient_and_price
            if check_in(ingregient_and_price, ingr_name):
                accumulated_price_per_ingr = int(ingregient_and_price[ingr_name])
                # скорей всего, цены на вновь встретившийся ингредиент в другом блюде нет
                ingr_price = set_and_get_nominal_price(ingredient)
                current_ingr_price = accumulated_price_per_ingr + ingr_price
                ingregient_and_price.update({ingr_name: current_ingr_price})
            else:
                ingr_price = set_and_get_nominal_price(ingredient)
                ingregient_and_price.update({ingr_name: ingr_price})

    ingregient_and_price_sorted = {k: ingregient_and_price[k] 
                                   for k in sorted(ingregient_and_price)}
    ingrs_and_prices = (ingregient_and_price_sorted.keys(),
                        ingregient_and_price_sorted.values())
    blank_table = dict(zip(column_names, ingrs_and_prices))
    ingredients = tabulate(blank_table, headers='keys', tablefmt=tablefmt)

    return ingredients


def main():
    dishes = get_dishes_from(config.FILENAME)

    ingrs = get_ingredients(dishes)

    print(ingrs)


if __name__ == '__main__':
    main()
