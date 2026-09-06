# Проверка задания

1. **Django-проект создан**
   - `manage.py`
   - `first_project/settings.py`
   - `first_project/urls.py`

2. **Созданы 3 статические страницы через `django.contrib.flatpages`**
   - `/about/`
   - `/styled/`
   - `/private/`
   - Записи создаются воспроизводимо миграцией `fpages/migrations/0001_seed_flatpages.py`.

3. **`{{ flatpage.content }}` повторяется два раза без изменения `content`**
   - `templates/flatpages/styled.html`
   - В шаблоне ровно два непосредственных вывода `{{ flatpage.content }}`.

4. **Одна страница доступна только админу / вошедшему пользователю**
   - `/private/` имеет `registration_required=True`.
   - Дополнительно URL защищён `staff_member_required`, поэтому в буквальном смысле доступ есть только active staff/admin.
   - Для проверки создайте администратора командой `python manage.py createsuperuser`.

5. **Изменены шрифты и размеры текста**
   - `static/css/site.css`
   - На `/styled/` явно заданы `font-family` и `font-size` для нескольких элементов.

6. **Bootstrap-шаблон с пользовательскими данными**
   - Общий шаблон: `templates/flatpages/default.html`
   - Используются Bootstrap navbar, cards, grid, buttons и данные `flatpage.title` / `flatpage.content`.

7. **Bootstrap подключён через Django static**
   - В шаблонах есть `{% load static %}`.
   - CSS и JS подключены через `{% static '...' %}`.
   - Bootstrap хранится локально в `static/vendor/bootstrap/`.
