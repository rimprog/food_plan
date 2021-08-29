"""

Принимает данные от П-я в виде одной из 3-х команд
Формирует ответ в виде таблиц

"""


import config
import helper_by_weekly_menu, \
       helper_by_ingredient, \
       helper_by_daily_menu
from utils import create_parser, \
                  get_dishes_from


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
    elif command_name_from_user == ingredient:
        ingredients = helper_by_ingredient.get_ingredients(dishes)
        print(ingredients)
    elif command_name_from_user == dailymenu:
        dailymenu = helper_by_daily_menu.get_recipes(dishes)
        print(*dailymenu)


if __name__ == '__main__':
    main()
