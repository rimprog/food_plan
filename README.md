# Food Plan
Командный проект № 1 курса от devman

## Описание

Составитель домашнего меню


### Особенности

* предоставляет возможность:
    - сформировать меню на неделю на основе [каталога блюд](https://github.com/rimprog/food_plan/wiki/Home/_edit),
    - получения [прайс-листа](https://github.com/rimprog/food_plan/wiki/Home/_edit),
    - узнать рецепты блюд:
        + на неделю,
        + на день/несколько дней/неделю.
* образует каталог блюд посредством [парсинга](https://github.com/rimprog/food_plan/edit/master/README.md).


## Сценарии работы

### Легенда "А"

#### Часть 1
Пользователь решил придерживаться разнообразного питания.
Утилиту можно использовать для составления меню на неделю.
Далее, Пользователь желает оценить, в какую сумму обойдутся ингредиенты
для блюд (на неделю). Взяв с собой, полученный через утилиту, прайс-лист, 
он приобретает ингредиенты и приступает к приготовлению.
Перед приготовлением, утилита, любезно предоставляет рецепты блюд на день/несколько дней/неделю.

**Сочетания подаваемых команд утилите, для реализации вышеописанной легенды:**
- weeklymenu & ingredient & dailymenu -day 1
- weeklymenu & ingredient & dailymenu -day 4
- weeklymenu & ingredient & dailymenu


#### Часть 2
Пользователь готовится к визиту гостей и хочет приготовить авторское блюдо.
Утилита поможет ему, выдав рецепт случайного блюда из каталога.

**Сочетания подаваемых команд утилите, для реализации вышеописанной легенды:**
- randomdailymenu


### Примеры работы утилиты

Выдача Пользователю меню на неделю:
![f](https://github.com/rimprog/food_plan/blob/I/O_examples/screenshots/dishes_a_week.JPG)

Выдача прай-листа:
![s](https://github.com/rimprog/food_plan/blob/I/O_examples/screenshots/price_list_a_week.JPG)

Рецепты блюд на день:
![t](https://github.com/rimprog/food_plan/blob/I/O_examples/screenshots/dishes_a_day.JPG)


### Используемые технологии

* [tabulate](https://pypi.org/project/tabulate/)
* [shelve](https://docs.python.org/3/library/shelve.html)
* [requests](https://docs.python-requests.org/en/master/)
* [tqdm](https://pypi.org/project/tqdm/)


### Требования к окружению

* Python 3.7 и выше,
* Linux/Windows.


#### Параметры проекта



### Установка

```bash
git clone https://github.com/rimprog/food_plan.git
cd food_plan
```
создание каталога виртуального окружения (ВО)*
`mkvirtualenv -p` <path> <virtualenv's_name>
связывание каталогов ВО и проекта
`setvirtualenvproject` <virtualenv's_path> <project's_path>
```bash
pip install -r requirements.txt
```
запуск скрипта
`python food_plan.py` <command_name>


### Пример запуска

```bash
python food_plan.py weeklymenu
python food_plan.py ingredient
python food_plan.py dailymenu -day 1
```





\* с использованием [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html)
