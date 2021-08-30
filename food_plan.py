"""

Принимает данные от П-я в виде команд и отрабатывает
    согласно логике, предусмотренной сценарием.
Формирует ответ в виде таблиц

Работает со списком блюд, образованным случайным образом
"""


import config
import helper_by_weekly_menu, \
       helper_by_ingredient, \
       helper_by_daily_menu
import shelver
from utils import create_parser, \
                  get_dishes_from, \
                  get_prepared_for_menu


def main():

    weeklymenu = config.COMMANDS_NAMES[0]
    ingredient = config.COMMANDS_NAMES[1]
    dailymenu = config.COMMANDS_NAMES[2]

    dishes = get_dishes_from(config.FILENAME)

    parser = create_parser()
    namespace = parser.parse_args()
    command_name_from_user = namespace.command_name


    if command_name_from_user == weeklymenu:
        weekmenu = helper_by_weekly_menu.get_weekmenu(dishes)
        print(weekmenu)
        shelver.update_dishes(config.SHELVE_FILENAME, dishes)
    elif command_name_from_user == ingredient:
        dishes = shelver.get_dishes(config.SHELVE_FILENAME)
        ingredients = helper_by_ingredient.get_ingredients(dishes)
        print(ingredients)
    elif command_name_from_user == dailymenu and namespace.day is not None:
        dishes = shelver.get_dishes(config.SHELVE_FILENAME)
        dailymenu = helper_by_daily_menu.get_recipes(dishes)
        print(*dailymenu)
        shelver.delete_dishes(config.SHELVE_FILENAME)
    elif command_name_from_user == dailymenu and namespace.day is None:
        dailymenu = helper_by_daily_menu.get_recipes(dishes)
        print(*dailymenu)


if __name__ == '__main__':
    main()
