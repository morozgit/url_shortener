# Микросервис для сокращения ссылок


## Установка 

Установите [python3](https://realpython.com/installing-python/).

## Репозиторий
Клонируйте репозиторий в удобную папку.

## Виртуальное окружение
В терминале перейдите в папку с репозиторием.

### Создание виртуального окружения
```bush 
python3 -m src/venv venv
```

### Активация виртуального окружения Linux

```bush
source src/venv/bin/activate
```


### Установка библиотек

```bush 
pip3 install -r requirements.txt
```
## Переменные окружения

### Создайте два файла в корне проекта
Примеры

- .env
  ```
    DB_HOST=localhost
    DB_PORT=5432
    DB_USER=postgres
    DB_PASS=postgres
    DB_NAME=url_shortener
  ```

  - .env.docker
  ```
    DB_HOST=postgres
    DB_PORT=5432
    DB_USER=postgres
    DB_PASS=postgres
    DB_NAME=url_shortener
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_DB=url_shortener
  ```

## Запуск


- Из корня проекта сделайте миграцию 

```bash
alembic upgrade head 
```

Запустить 
```bash
python3 src/main.py
```

## Запуск в Docker
Установить [Docker](https://docs.docker.com/engine/install/ubuntu/)

Установить [Docker compose](https://docs.docker.com/compose/install/linux/)

Из корня проекта запустить
```
docker compose up --build
```