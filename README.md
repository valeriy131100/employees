# employees

Сайт с древовидным представлением сотрудников.

## Быстрый запуск dev-версии с помощью docker-compose

Вам понадобится установленный [Docker](https://docs.docker.com/get-docker/) и git.

Склонируйте репозиторий:
```bash
$ git clone https://github.com/valeriy131100/employees
```

Находясь в директории employees исполните:
```bash
$ docker-compose build && docker-compose up -d
```

Сайт запустится по адресу [127.0.0.1:8000](http://127.0.0.1:8000).

Также он будет сразу заполнен тестовыми данными.

## Установка
Вам понадобится установленный Python 3.8+ и git.

Склонируйте репозиторий:
```bash
$ git clone https://github.com/valeriy131100/employees
```

Создайте в этой папке виртуальное окружение:
```bash
$ cd employees
$ python3 -m venv venv
```

Активируйте виртуальное окружение и установите зависимости:
```bash
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Использование

### Переменные среды
Заполните файл .env.example и переименуйте его в .env или иным образом задайте переменные среды:
* `DEBUG` - включен ли режим дебага в Django. По умолчанию - `True`.
* `ALLOWED_HOSTS` — [см. документацию Django](https://docs.djangoproject.com/en/4.0/ref/settings/#allowed-hosts). По умолчанию - `127.0.0.1`.
* `SECRET_KEY` - секретный ключ отвечающий за шифрование. По умолчанию - `REPLACE_ME`. 

### Миграции базы данных
Перед тем как запускать сайт нужно применить миграции базы данных. Находясь в директории employees исполните:
```bash
$ venv/bin/python manage.py migrate
```

### Заполнение фейковыми данными
Находясь в директории employees исполните:
```bash
$ venv/bin/python manage.py seed
```

Будет создано 50000 случайных сотрудников с 5 уровнями иерархии.

### Запуск сайта
Находясь в директории employees исполните:
```bash
$ venv/bin/python manage.py runserver
```

Сайт запустится по адресу [127.0.0.1:8000](http://127.0.0.1:8000).

Можно указать желаемый IP-адрес и порт:
```bash
$ venv/bin/python manage.py runserver 127.0.0.1:8000
```
