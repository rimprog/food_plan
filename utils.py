import argparse
from itertools import chain
import json
import random
from typing import Dict, List

import config


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('command_name',
                        choices=config.COMMANDS_NAMES,
                        help='Определяет название команды')
    parser.add_argument('-day',
                        type=int,
                        help='Определяет кол-во дней, для которых предоставить рецепты')

    return parser


def get_dishes_from(filename):
    with open(filename, 'rt') as f:
        dishes = json.load(f)

        return dishes


def check_in(iterable: Dict[str, int], name):
    in_iterable = name in iterable

    return in_iterable


def get_renamed_column(column_name: tuple,
                       with_new_column: str) -> str:
    
    column_name += (with_new_column, )
    col_name = ' '.join(list(column_name))

    return col_name


def get_prepared_for_menu(dishes: List[Dict],
                          categories_names=('Завтрак', 'Обед', 'Ужин', ),
                          days=7) -> List[Dict]:
    
    """Расставляет блюда в порядке, соответствующем именам категорий."""

    random.shuffle(dishes)

    categories_with_dishes = [list() for _ in categories_names]
    category_name_and_cipher = dict(zip(categories_names, range(len(categories_names))))

    for dish in dishes:
        category_name = dish['type']
        category_cipher = category_name_and_cipher[category_name]
        dishes_per_category = categories_with_dishes[category_cipher]
        if days != len(dishes_per_category):  # категория НЕ заполнена нужным кол-вом блюд
            dishes_per_category.append(dish)
            continue
        elif len(categories_names) * days == len(list(chain.from_iterable(categories_with_dishes))):
            break  # Все категории заполнены блюдами
    
    time_intervals_with_dishes = zip(*categories_with_dishes)
    dishes_per_days = [z for zip_ in time_intervals_with_dishes for z in zip_]

    return dishes_per_days
