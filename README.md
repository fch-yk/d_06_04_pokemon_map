# Map of pokemons

The Django-based site renders [pokemons](https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%BA%D0%B5%D0%BC%D0%BE%D0%BD) on the map.

## Prerequisites

Python 3.7 is required. You can download it [here](https://www.python.org/downloads/release/python-379/)

## Installing

- Download the project files
- Set up packages:

```bash
pip install -r requirements.txt
```

- Set up environmental variables in your operating system or in .env file. The variables are:

  - `DEBUG` (optional, `True` by default)
  - `SECRET_KEY` (optional, `REPLACE_ME` by default)
  - `ALLOWED_HOSTS` (obligatory when `DEBUG` is set to `False`)
  - `TIME_ZONE` (optional, `Europe/Moscow` by default)

To set up variables in .env file, create it in the root directory of the project and fill it up like this:

```bash
DEBUG=True
SECRET_KEY=REPLACE_ME
ALLOWED_HOSTS=localhost,127.0.0.1
TIME_ZONE=Europe/Moscow
```

### Как запустить

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Затем установите зависимости

```sh
pip install -r requirements.txt
```

Запустите разработческий сервер

```sh
python3 manage.py runserver
```

### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 2 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
