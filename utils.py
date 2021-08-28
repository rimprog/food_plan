import argparse
import json

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
