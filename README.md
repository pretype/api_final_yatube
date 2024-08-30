# api_final
api final

## Описание

Приложение Ya_tube, 

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/pretype/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
py -m venv venv
```

```
. venv/String/activate
```

Установить зависимости из файла requirements.txt:

```
py -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
py manage.py migrate
```

Запустить проект:

```
py manage.py runserver
```

## Техническая документация

```
После запуска проекта, техническая документация будет доступна по ссылке: http://127.0.0.1:8000/redoc/
```

## Примеры: 

Все операции осуществлять после запуска проекта.

```
Получить список постов можно методом GET по ссылке: http://127.0.0.1:8000/api/v1/posts/
```

```
Зарегистрировать учетную запись, можно методом POST по ссылке: http://127.0.0.1:8000/api/v1/jwt/me/
Для входа потребуется передать (данные/техническое наименование/тип данных):
логин - username - string (обязательное поле);
пароль - password - string (обязательное поле).
```

```
Создать свой пост, можно методом POST по ссылке: http://127.0.0.1:8000/api/v1/posts/
Для создания нужно войти под зарегистрированной учетной записью и передать 
следующие данные (данные/техническое наименование/тип данных): 
текст публикации - text - string (обязательное поле);
изображение - image - string or null <binary>;
id сообщества - group - integer or null.
```