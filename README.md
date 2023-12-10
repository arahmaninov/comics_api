# comics_api

## о приложении

Тестовое задание на реализацию системы оценки и отображения комиксов.
ТЗ: https://pastebin.com/j2jtK3M8

API endpoints:

/api/ratings/ (post)

/api/comics/<comic_id>/rating/ (get)

В бд уже есть 3 тестовые записи комиксов и 4 записи оценок.

Использованные технологии: **fastapi, sqlalchemy, sqlite3, pytest.**


## установка

~~~
pip install -r requirements.txt
uvicorn app.main:app
~~~

Для запуска тестов:
~~~
pytest
~~~
