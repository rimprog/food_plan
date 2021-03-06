## Парсер рецептов с сайта delikateska

Скрипт `parse_delikateska_recipes.py` для парсинга рецептов с сайта доставки продуктов [delikateska](https://www.delikateska.ru/).

Чтобы отдельно запустить данный скрипт, проделайте следующие действия:
- Скачайте репозиторий с кодом, либо перейдите в его корневую директорию, если он уже скачан.
- Установите зависимости командой `pip install -r requirements.txt`.
- Запустите parse_delikateska_recipes.py командой `python3 parse_delikateska_recipes.py`.

Скрипт отправляет запросы в формате graphql и получает qraphql ответы, который сохраняется в формате json.

Итоговые результаты парсинга сохраняются в каталог `parsing_results`:
-  Файл `recipes.json` содержит результаты парсинга рецептов. [Пример рецепта](https://www.delikateska.ru/recipes/zapechennaya-noga-yagnenka-s-myatnym-sousom-3799)  собираемого с сайта.
-  Файл `recipes_catalog.json` содержит информацию по id всего количества запрошенных рецептов из [общего каталога рецептов сайта](https://www.delikateska.ru/recipes).

При простом вызове скрипта в консоле, происходит скачивание всех id рецептов (по умолчанию 736 штук) из раздела [Рецепты](https://www.delikateska.ru/recipes). Также при вызове скрипта в командной строке, можно передать необязательный аргумент `--count НУЖНОЕ_КОЛИЧЕСТВО_РЕЦЕПТОВ` для скачивания требуемого количества рецептов. Ниже пример вызова скрипта с указанием скачать 10 рецептов:

`python3 parse_delikateska_recipes.py --count 10`

После запуска скрипта, при его корректной работе по ходу скачивания, вам в консоль будет выводиться текущий прогресс закачки. Ниже пример вывода в консоль при успешном сценарии работы скрипта:
```
Recipes catalog parsed successfully! All data saved to recipes_catalog.json
100%|███████████████████████████████████████████| 10/10 [00:02<00:00,  4.04it/s]
10 recipes parsed successfully! All data saved to recipes.json
```
При появлении в консоле надписей с содержанием слова "Error", скрипт следует остановить и устранить причину возникновения ошибки, либо обратиться к [разработчику](https://github.com/rimprog).

## Скрипт для создания локальной базы рецептов

Скрипт `build_local_database.py` создает собственную локальную базу рецептов, наполняя ее рецептами полученными при помощи скрипта `parse_delikateska_recipes.py`.

Чтобы отдельно запустить данный скрипт, проделайте следующие действия:
- Скачайте репозиторий с кодом, либо перейдите в его корневую директорию, если он уже скачан.
- Установите зависимости командой `pip install -r requirements.txt`.
- Следуя [инструкции](https://github.com/rimprog/food_plan#%D0%BF%D0%B0%D1%80%D1%81%D0%B5%D1%80-%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82%D0%BE%D0%B2-%D1%81-%D1%81%D0%B0%D0%B9%D1%82%D0%B0-delikateska) текущей документации, посвященной работе скрипта `parse_delikateska_recipes.py`, получите файл `recipes.json`.
- Запустите build_local_database.py командой `python3 build_local_database.py`.

Скрипт помимо создания локальной базы данных рецептов, также дополняет информацию о рецептах. Через функцию `update_local_database` добавляется общая стоимость всех ингредиентов рецепта и принадлежность рецепта к одной из 3 категорий: Завтрак, Обед, Ужин.

При помощи функции `filter_local_database` скрипт производит фильтрацию созданной базы рецептов на предмет наличия всех цен на все ингридиенты и наличия указания категории у всех рецептов.

После запуска скрипта, при его корректной работе вы увидите следующий вывод в консоль:
```
Local database was created successfully.
Local database was updated successfully.
Local database was filtered successfully.
Local database was saved successfully to "recipes_database.json".
```
При появлении в консоле надписей с содержанием слова "Error", следует устранить причину возникновения ошибки и попробовать запустить скрипт снова. В случае, если самостоятельно устранить ошибку не удается, обратитесь к [разработчику](https://github.com/rimprog).

Итогово полученная локальная база данных рецептов сохраняется в файл `recipes_database.json` каталога `database` и представляет собой json файл, со следующими ключами (пример):
```
"title": "Паста с лисичками",
"difficult": 3,
"cooking_time": 15,
"servings_count": 2,
"image_link": "some_website/cache/f/9/0cde2d7f-a819-4fc9-847c-5fa379008a52.png/w480.png",
"ingredients": [
  {
    "title": "Итальянская паста на Ваш вкус",
    "count": "200г",
    "price": 139
  },
  {
    "title": "Сливки 10-20%",
    "count": "100г",
    "price": 173
  },
],
"instructions": [
  {
    "step_number": 1,
    "description": "Лук нарежем соломкой.",
    "image_link": "some_website/cache/1/3/d03d2f70-ecc0-474f-90b1-87c68cbbe5ab.png/w900h700.png"
  },
  {
    "step_number": 2,
    "description": "Помидоры черри разрежем пополам на 2 части, петрушку мелко порубим.",
    "image_link": "some_website/cache/5/b/af907077-5689-4d77-bc2f-cfc2be3e0c4d.png/w900h700.png"
  },
],
"type": "Завтрак",
"ingredients_price": 1440
```

## Цели проекта

Код написан в рамках командного проекта учебной программы от [новичка до Middle](https://dvmn.org/t/middle-python-dev-before-you-finish-the-course/) на онлайн курсах обучению программирования python [Devman](https://dvmn.org/).
