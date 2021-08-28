"""
Принимает данные от П-я в виде одной из 3-х команд
Формирует ответ в виде таблиц

"""


import config
import helper_by_weekly_menu, \
       helper_by_ingredient, \
       helper_by_daily_menu
from utils import create_parser


def main():

    weeklymenu = config.COMMANDS_NAMES[0]
    ingredient = config.COMMANDS_NAMES[1]
    dailymenu = config.COMMANDS_NAMES[2]

    dishes_names = [
        'breakfast dish',
        'dish for lunch',
        'dish for dinner'
    ]

    parser = create_parser()
    namespace = parser.parse_args()
    command_name_from_user = namespace.command_name

    if command_name_from_user == weeklymenu:
        weekmenu = helper_by_weekly_menu.get_weekmenu(dishes_names)
        print(weekmenu)
    elif command_name_from_user == ingredient:
        ingredients = helper_by_ingredient.get_ingredients(config.FILENAME)
        print(ingredients)
    elif command_name_from_user == dailymenu:
        daymenu = helper_by_daily_menu.get_daymenu_one_dish(config.FILENAME)
        print(daymenu)


if __name__ == '__main__':
    main()
