# Pokémon map

The Django-based site renders [Pokémon](https://en.wikipedia.org/wiki/Pok%C3%A9mon#Name) entities on the map.

## Prerequisites

Python 3.7 is required. You can download it [here](https://www.python.org/downloads/release/python-379/)

## Installing

- Download the project files
- It is recommended to use [venv](https://docs.python.org/3/library/venv.html?highlight=venv#module-venv) for project isolation
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

## Initializing a database

- Make migrations:

```bash
python manage.py makemigrations pokemon_entities
```

- Migrate:

```bash
python manage.py migrate
```

- Create a superuser:

```bash
python manage.py createsuperuser
```

## Using

- Run a development server:

```bash
python manage.py runserver
```

- Go to [the admin site](http://127.0.0.1:8000/admin/) and fill the base with Pokémon characteristics and entities
- Go to [the site main page](http://127.0.0.1:8000/)

## Project goals

The project was created for educational purposes.
It's a lesson for python and web developers at [Devman](https://dvmn.org)
