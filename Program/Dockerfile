# Запустимо нашу програму всередині контейнера
# Docker-команда FROM вказує базовий образ контейнера
FROM python:3.11
# Встановлюємо залежності
COPY ./Personal_assistant/Program/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Копіюємо файли у робочу директорію контейнера
COPY ./Personal_assistant/Program /app

# Задаємо робочу директорію
WORKDIR /app

# Запускаємо команду для запуску вашого коду
CMD ["python", "bot_interface.py"]
