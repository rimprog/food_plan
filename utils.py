import argparse
import json
import random
from typing import Dict, List

import config


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('command_name',
                        choices=config.COMMANDS_NAMES,
                        help='Определяет название команды')
    parser.add_argument('-day', help='Определяет день недели')  # , default='Понедельник'

    return parser


def get_dishes_from(filename):
    with open(filename, 'rt') as f:
        dishes = json.load(f)

        return dishes


def get_fitted_cell_size(line, symbols_in_new_word=20):

    lines_words = line.split()
    sub_new_word_template = '{word} '

    if len(line) <= symbols_in_new_word:
        return line
    else:
        new_word = ''
        new_words_of_new_line = []
        for idx, word in enumerate(lines_words):
            sub_new_word = sub_new_word_template.format(word=word)
            if len(new_word) + len(sub_new_word) < symbols_in_new_word:
                new_word += sub_new_word
            elif idx == len(lines_words) - 1:
                new_words_of_new_line.append(new_word)
            else:
                new_word += '\n'
                new_words_of_new_line.append(new_word)
                new_word = ''
                new_word += sub_new_word

        new_line = ''.join(new_words_of_new_line)

    return new_line


def check_in(iterable: Dict[str, int], name):
    in_iterable = name in iterable

    return in_iterable


def set_and_get_nominal_price(ingredient: Dict) -> int:
    try:
        ingr_price = int(ingredient['ingredientsItems'][0]
                        ['catalogItem']['currentPriceField2'])
    except IndexError:  # Нет информации о цене
        ingr_price = 1  # Номинальная цена любого ингредиента

    return ingr_price


def get_renamed_column(column_name: tuple, with_new_column: str) -> str:
    column_name += (with_new_column, )
    col_name = ' '.join(list(column_name))

    return col_name


def get_prepared_for_menu(dishes: List[Dict],
                          categories_names=('Завтрак', 'Обед', 'Ужин', ),
                          days=7) -> List[Dict]:
    
    """Расставляет блюда в порядке, соответствующем именам категорий."""

    random.shuffle(dishes)

    categories_with_dishes = [list() for _ in categories_names]  #FIXME
    category_name_and_cipher = dict(zip(categories_names, range(len(categories_names))))

    for dish in dishes:
        category_name = dish['type']
        category_cipher = category_name_and_cipher[category_name]
        dishes_per_category = categories_with_dishes[category_cipher]
        if days != len(dishes_per_category):  # категория НЕ заполнена нужным кол-вом блюд
            dishes_per_category.append(dish)
            continue
        break  # как только все категории заполнятся
    
    time_intervals_with_dishes = zip(*categories_with_dishes)
    dishes_per_days = [z for z in zip_ for zip_ in time_intervals_with_dishes]

    return dishes_per_days
