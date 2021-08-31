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
    randomdailymenu = config.COMMANDS_NAMES[3]

    dishes = get_dishes_from(config.FILENAME)
    dishes_to_menu = get_prepared_for_menu(dishes)

    parser = create_parser()
    namespace = parser.parse_args()
    command_name_from_user = namespace.command_name
    days_to_show_menu = namespace.day

    if command_name_from_user == weeklymenu:
        weekmenu = helper_by_weekly_menu.get_weekmenu(dishes_to_menu)
        print(weekmenu)
        shelver.delete_dishes(config.SHELVE_FILENAME)
        shelver.update_dishes(config.SHELVE_FILENAME, dishes_to_menu)
    elif command_name_from_user == ingredient:
        prepared_dishes = shelver.get_dishes(config.SHELVE_FILENAME)
        ingredients = helper_by_ingredient.get_ingredients(prepared_dishes)
        print(ingredients)
    elif command_name_from_user == dailymenu and days_to_show_menu is not None:  # dailymenu -day 2
        prepared_dishes = shelver.get_dishes(config.SHELVE_FILENAME)
        dailymenu = helper_by_daily_menu.get_recipes(prepared_dishes, for_days=days_to_show_menu)
        print(*dailymenu)
        shelver.delete_dishes(config.SHELVE_FILENAME)
    elif command_name_from_user == dailymenu and days_to_show_menu is None:  # dailymenu
        prepared_dishes = shelver.get_dishes(config.SHELVE_FILENAME)
        dailymenu = helper_by_daily_menu.get_recipes(prepared_dishes, for_days=7)
        print(*dailymenu)
    elif command_name_from_user == randomdailymenu:
        # Сделать 3 блюда на день
        dailymenu = helper_by_daily_menu.get_recipes(dishes_to_menu, for_days=1, with_dishes_in_day=1)
        print(*dailymenu)


if __name__ == '__main__':
    main()
