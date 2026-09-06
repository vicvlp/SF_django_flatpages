# SkillFactory Django FlatPages

Небольшой учебный Django-проект, вариант задания по FlatPages, Bootstrap и static-файлам.

## Что реализовано

- Django-проект и приложение `fpages`.
- Ровно 3 записи `FlatPage`: `/about/`, `/styled/`, `/private/`.
- На `/styled/` `{{ flatpage.content }}` выведен ровно два раза.
- На `/styled/` явно изменены `font-family` и `font-size` через `static/css/site.css`.
- `/private/` помечена `registration_required=True` и дополнительно защищена `staff_member_required`.
- Bootstrap 5.3.6 хранится локально и подключается только через `{% load static %}` и `{% static %}`.
- Есть автоматические тесты всех ключевых требований.

## Запуск на Windows

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Открыть:

- `http://127.0.0.1:8000/about/`
- `http://127.0.0.1:8000/styled/`
- `http://127.0.0.1:8000/private/`
- `http://127.0.0.1:8000/admin/`

`/private/` потребует входа под пользователем с правами staff/admin.

## Автоматическая проверка

После установки зависимостей и миграций:

```powershell
python manage.py test
python manage.py check
```

Подробное соответствие пунктам задания находится в `CHECKLIST.md`.

## Почему `db.sqlite3` не хранится в Git

Статические страницы создаются data migration `fpages/migrations/0001_seed_flatpages.py`. Поэтому результат воспроизводим после обычного `python manage.py migrate`, а локальная база и учётные данные администратора не попадают в репозиторий.
