# Базовый образ 
FROM python:3.12-slim

# запретит внутри контейнера создавать файлы с кешем
ENV PYTHONDONTWRITEBYTECODE=1

ENV DJANGO_SETTINGS_MODULE=Marketplace.settings

# делает так, что Python сразу выводит сообщения в консоль, без задержки в буфере
ENV PYTHONUNBUFFERED=1

# Папка в которой будет храниться приложение
WORKDIR /app

# Обновляет pip внутри контейнера 
RUN pip install --upgrade pip

# копирует этот файл из локальной машины в контейнер, будет использоваться для установки зависимостей
COPY requirements.txt .

# установка зависимостей проекта
RUN pip install -r requirements.txt

# Команда для копирования файлов и папок с ПК в контейнер
COPY . . 

# говорит какой порт надо открыть контейнеру 
EXPOSE 8000

# Команда для запуска Daphne ASGI сервера

CMD ["sh", "-c", "python3 manage.py migrate --noinput && gunicorn Marketplace.wsgi:application -b 0.0.0.0:8000"]

