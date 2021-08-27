import os
import json

import requests
from tqdm import tqdm


def check_errors(response):
    errors = response.json().get('errors')

    if errors:
        raise requests.HTTPError(f'Error. HTTP 400 Found. Incorrect graphql query.\nServer response: {errors}')


def parse_recipes_catalog(recipes_count):
    url = 'https://new-api.delikateska.ru/graphql'

    graphql_query = {
        'query': '''{
                      getRecipesWithFilters( page:1, setLimit: '''+ str(recipes_count) +''') {
                        typesItems {
                          id
                          title
                        }
                        slozhnostItems {
                          id
                          title
                        }
                        bludoItems {
                          id
                          title
                        }
                        obrabotkaItems {
                          id
                          title
                        }
                        naznachenieItems {
                          id
                          title
                        }
                        totalCount
                        recipeItems {
                          id
                          isFavorite
                          title
                          identifyIdURI
                          rating
                          text
                          comments_number
                          date
                          author
                          recipes_difficult #  иконка с шапкой повара. от 1-го до 5
                          slozhnostItem {
                            id
                            title
                          }
                          cooking_time # время приготовления
                          rating # если 0, то "не оценен" https://www.delikateska.ru/recipes/1775
                          serving # порции
                          attachmentsItem {
                            cacheItem {
                              filePath # путь карлито
                            }
                          }
                          bludoItem {
                            id
                            title
                          }
                        }
                      }
                    }
                    '''
    }

    response = requests.post(url, json=graphql_query)
    response.raise_for_status()
    check_errors(response)

    recipes_catalog = response.json()

    return recipes_catalog


def get_recipes_ids(recipes_catalog):
    recipes_ids = []
    for recipe in recipes_catalog['data']['getRecipesWithFilters']['recipeItems']:
        recipes_ids.append(recipe['id'])

    return recipes_ids


def parse_recipe(recipe_id):
    url = 'https://new-api.delikateska.ru/graphql'

    graphql_query = {
        'query': '''{
                      getRecipeById(id: ''' + str(recipe_id) + ''', imageSizeFilter: "w480") {
                        id
                        tip
                        isFavorite
                        title
                        rating
                        author
                        comments_number
                        text
                        _votedRating
                        date
                        recipes_difficult #  иконка с шапкой повара. от 1-го до 5
                        slozhnostItem {
                          id
                          title
                        }
                        cooking_time # время приготовления
                        rating # если 0, то "не оценен" https://www.delikateska.ru/recipes/1775
                        serving # порции
                        attachmentsItem {
                          cacheItem {
                            filePath # путь карлито
                          }
                        }
                        recipeIngredients {
                          id
                          title
                          value
                          ##!! Всегда брать первый элемент !!##
                          ingredientsItems {
                            catalogItem {
                              id
                              available
                              currentPriceField
                              currentPriceField2
                              symbolPriceField
                              ## catalogItem('list')
                            }
                          }
                        }
                        recipeInstructions {
                          id
                          title # описание инструкции
                          ##!! Всегда брать первый элемент !!##
                          fileItem {
                            cacheItem {
                              filePath # путь картинки для элемента инструкции
                            }
                          }
                        }
                      }
                    }
                  '''
    }

    response = requests.post(url, json=graphql_query)
    response.raise_for_status()
    check_errors(response)

    recipe = response.json()

    return recipe


def save_parsing_results(parsing_results, filename):
    save_folder_name = 'parsing_results'
    parsing_results_path = os.path.join(save_folder_name, filename)

    os.makedirs(save_folder_name, exist_ok=True)
    with open(parsing_results_path, 'w', encoding='utf-8') as my_file:
        json.dump(parsing_results, my_file, ensure_ascii=False)


def main():
    recipes_count = 736
    recipes_catalog = parse_recipes_catalog(recipes_count)
    recipes_catalog_filename = 'recipes_catalog.json'

    save_parsing_results(recipes_catalog, recipes_catalog_filename)
    print(f'Recipes catalog parsed successfully! All data saved to {recipes_catalog_filename}')

    recipes_ids = get_recipes_ids(recipes_catalog)

    recipes_filename = 'recipes.json'
    recipes = []
    for recipe_id in tqdm(recipes_ids):
        try:
            recipe = parse_recipe(recipe_id)
            recipes.append(recipe)
        except requests.HTTPError as error:
            print(error)
            continue

    save_parsing_results(recipes, recipes_filename)
    print(f'{len(recipes)} recipes parsed successfully! All data saved to {recipes_filename}')


if __name__ == '__main__':
    main()
