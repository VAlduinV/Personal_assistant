# Запустимо нашу програму всередині контейнера
# Docker-команда FROM вказує базовий образ контейнера
FROM python:3.11
# Встановлюємо залежності
# Встановлюємо пакунок xvfb
RUN apt-get update && apt-get install -y xvfb
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt
COPY . /app
WORKDIR /app
CMD ["xvfb-run", "python", "bot_interface.py"]
