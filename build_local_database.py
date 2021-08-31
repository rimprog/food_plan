import os
import json
import random


def load_json(file_path):
    with open(file_path, encoding="utf-8") as json_file:
        json_file_content = json.load(json_file)

    return json_file_content


def save_local_database(local_database, filename):
    save_folder_name = 'database'
    local_database_path = os.path.join(save_folder_name, filename)

    os.makedirs(save_folder_name, exist_ok=True)
    with open(local_database_path, 'w', encoding='utf-8') as my_file:
        json.dump(local_database, my_file, ensure_ascii=False)


def get_recipe_ingredients(parsed_recipe_ingredients):
    ingredients = []
    for ingredient in parsed_recipe_ingredients:
        title = ingredient['title']
        count = ingredient['value']
        price = ingredient['ingredientsItems'][0]['catalogItem']['currentPriceField2'] if ingredient['ingredientsItems'] else None

        ingredient = {
            'title': title,
            'count': count,
            'price': price
        }

        ingredients.append(ingredient)

    return ingredients


def get_recipe_insrtuction_steps(parsed_recipe_instruction):
    instruction_steps = []
    for step_number, instruction_step in enumerate(parsed_recipe_instruction, 1):
        description = ' '.join(instruction_step['title'].strip().split('\r\n'))
        image_link = instruction_step['fileItem']['cacheItem'][1]['filePath'] if instruction_step['fileItem'] else None

        instruction_step = {
        'step_number': step_number,
        'description': description,
        'image_link': image_link
        }

        instruction_steps.append(instruction_step)

    return instruction_steps


def create_local_database(parsed_recipes):
    local_database = []
    for recipe in parsed_recipes:
        title = recipe['data']['getRecipeById']['title']
        difficult = recipe['data']['getRecipeById']['recipes_difficult']
        cooking_time = recipe['data']['getRecipeById']['cooking_time']
        servings_count = recipe['data']['getRecipeById']['serving']
        image_link = recipe['data']['getRecipeById']['attachmentsItem']['cacheItem'][0]['filePath']
        ingredients = get_recipe_ingredients(recipe['data']['getRecipeById']['recipeIngredients'])
        instructions = get_recipe_insrtuction_steps(recipe['data']['getRecipeById']['recipeInstructions'])

        recipe = {
            'title': title,
            'difficult': difficult,
            'cooking_time': cooking_time,
            'servings_count': servings_count,
            'image_link': image_link,
            'ingredients': ingredients,
            'instructions': instructions
        }

        local_database.append(recipe)

    return local_database


def add_recipes_types(recipes):
    recipe_types = ['Завтрак', 'Обед', 'Ужин']
    max_count_one_recipe_type = len(recipes) / len(recipe_types)
    random.seed(a=2)

    recipes_with_types = []
    for recipe in recipes:
        if recipe['cooking_time']:
            recipe['type'] = recipe_types[0] if recipe['cooking_time'] < 20 else random.choice(recipe_types[1:])
        else:
            recipe['type'] = None

        recipes_with_types.append(recipe)

    return recipes_with_types


def add_recipes_costs(recipes):
    recipes_with_costs = []
    for recipe in recipes:
        ingredients_prices = [ingredient['price'] if ingredient['price'] else 0 for ingredient in recipe['ingredients']]
        sum_ingredients_prices = sum(ingredients_prices)

        recipe['ingredients_price'] = sum_ingredients_prices

        recipes_with_costs.append(recipe)

    return recipes_with_costs


def update_local_database(local_database):
    updated_recipes = add_recipes_types(local_database)
    updated_recipes = add_recipes_costs(local_database)

    return updated_recipes


def check_existence_all_ingredients_prices(recipe):
    ingredients = recipe['ingredients']

    for ingredient in ingredients:
        if not ingredient['price']:
            return False
    return True


def filter_local_database(local_database, is_all_ingredients_prices=True, is_all_recipes_types=True):
    if is_all_ingredients_prices:
        filtered_local_database = filter(check_existence_all_ingredients_prices,
                                         local_database)

    if is_all_recipes_types:
        filtered_local_database = filter(lambda recipe: recipe['type'],
                                         filtered_local_database)

    filtered_local_database = list(filtered_local_database)

    return filtered_local_database


def main():
    parsed_recipes_path = os.path.join('parsing_results', 'recipes.json')
    parsed_recipes = load_json(parsed_recipes_path)

    local_database = create_local_database(parsed_recipes)

    updated_local_database = update_local_database(local_database)

    filtered_local_database = filter_local_database(updated_local_database)

    local_database_name = 'recipes_database.json'
    save_local_database(filtered_local_database, local_database_name)


if __name__ == '__main__':
    main()
