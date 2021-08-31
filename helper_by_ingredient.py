from typing import List, Dict

from tabulate import tabulate

import config
from utils import check_in, \
                  get_dishes_from


def get_ingredients(dishes: List[Dict],
                    column_names=('Ингредиент', 'Цена, руб.'),
                    tablefmt='grid'):

    """Формирует прайс-лист, отсортированный по названиям ингредиентов"""

    ingregient_and_price = {}
    for dish in dishes:
        ingrs_per_dish = dish['ingredients']
        for ingredient in ingrs_per_dish:
            ingr_name = ingredient['title']
            ingr_price = int(ingredient['price'])
            # Ингредиент уже встречался в предыдущих блюдах
            if check_in(ingregient_and_price, ingr_name):
                accumulated_price_per_ingr = int(ingregient_and_price[ingr_name])
                current_ingr_price = accumulated_price_per_ingr + ingr_price
                ingregient_and_price.update({ingr_name: current_ingr_price})
            else:
                ingregient_and_price.update({ingr_name: ingr_price})

    ingregient_and_price_sorted = {k: ingregient_and_price[k] 
                                   for k in sorted(ingregient_and_price)}
    ingrs_and_prices = (ingregient_and_price_sorted.keys(),
                        ingregient_and_price_sorted.values())
    blank_table = dict(zip(column_names, ingrs_and_prices))
    ingredients = tabulate(blank_table, headers='keys', tablefmt=tablefmt)

    return ingredients


def main():
    dishes = get_dishes_from(config.DELIKATESKA_FILENAME)

    ingrs = get_ingredients(dishes)

    print(ingrs)


if __name__ == '__main__':
    main()
