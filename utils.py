import argparse
import json
from typing import Dict

import config


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('command_name',
                        choices=config.COMMANDS_NAMES,
                        help='Определяет название команды')

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
