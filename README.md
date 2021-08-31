# Генератор меню на неделю с общей ценой закупки продуктов

TODO: Общее описание проекта

## parse_delikateska_recipes.py

Скрипт для парсинга рецептов с сайта доставки продуктов [delikateska](https://www.delikateska.ru/)

Чтобы отдельно запустить данный скрипт, проделайте следующие действия:
- Скачайте репозиторий с кодом, либо перейдите в его корневую директорию, если он уже скачан.
- Установите зависимости командой `pip install -r requirements.txt`.
- Запустите parse_delikateska_recipes.py командой `python3 parse_delikateska_recipes.py`.

Скрипт отправляет запрос в формате graphql и получает qraphql ответ, который сохраняется в формате json.

Итоговые результаты парсинга сохраняются в каталог `parsing_results`:
-  Файл `recipes.json` содержит результаты парсинга рецептов.
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

## Цели проекта

Код написан в рамках командного проекта учебной программы от [новичка до Middle](https://dvmn.org/t/middle-python-dev-before-you-finish-the-course/) на онлайн курсах обучению программирования python [Devman](https://dvmn.org/).