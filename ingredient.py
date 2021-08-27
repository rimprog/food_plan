import argparse
import json

from tabulate import tabulate


def get_ingredients(filename,
                    ingrs_names=None,
                    prices=None,
                    column_names=('Ингредиент', 'Цена'),
                    tablefmt='grid'):

    ingrs_names, prices = None or [], None or []

    dish = get_dish_from(filename)
    ingrs = dish['data']['getRecipeById']['recipeIngredients']
    for ingredient in ingrs:
        ingr_name = ingredient['title']
        ingrs_names.append(ingr_name)
        try:
            ingr_price = ingredient['ingredientsItems'][0]['catalogItem']['currentPriceField2']
        except IndexError:  # Нет информации о цене
            ingr_price = 1  # Номинальная цена любого ингредиента
        prices.append(ingr_price)
    
    ingrs_and_prices = (ingrs_names, prices)
    blank_table = dict(zip(column_names, ingrs_and_prices))

    ingredients = tabulate(blank_table, headers='keys', tablefmt=tablefmt)
        
    return ingredients


def get_dish_from(filename):
    with open(filename, 'rt') as f:
        dish = json.load(f)

        return dish


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('ingredient', help='Команда `ingredient`')

    return parser


def main():
    filename = 'dish.json'

    ingrs = get_ingredients(filename)

    print(ingrs)



if __name__ == '__main__':
    main()
