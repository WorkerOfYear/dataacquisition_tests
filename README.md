# Задача
Сделать панель администратора для управления записями в базе данных. Требования:
1. Страница с дашбордом в которой будут находится 2 карточки с общим количеством Юзеров и Предметов (Items)
2. Поля моделей должны распаршиваться автоматически, и отображаться в таблице пользовательского интерфейса как новая колонка
3. Редактирование видимости полей из пункт 2 в пользовательском интерфейсе
4. Результат отображения модели в интерфейсе ‐ таблица с записями из базы данных
5. Для каждой записи должны присутствовать 3 кнопки : удалить запись, добавить запись, редактировать запись
6. Система авторизации Логин+Пароль


# Setup

The first thing to do is to clone the repository:

    git clone https://github.com/WorkerOfYear/dataacquisition_tests.git
    cd dataacquisition_tests

Create a virtual environment to install dependencies in and activate it:

    pip -m venv venv

Activate

    source venv/bin/activate

Install dependencies

    pip install -r requirements.txt

Run

    python manage.py runserver
    
<p>And navigate to http://127.0.0.1:8000/.</p>





