# Docker-команда FROM вказує базовий образ контейнера
# Наш базовий образ - це Linux з попередньо встановленим python-3.10
FROM python:3.10 AS build-env

# Встановимо робочу директорію всередині контейнера
WORKDIR /app/

# Встановимо змінну середовища
ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app/

# Запустимо наш застосунок всередині контейнера
CMD ["python", "main:app"]