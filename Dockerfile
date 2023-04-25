# Запустимо нашу програму всередині контейнера
# Docker-команда FROM вказує базовий образ контейнера
FROM python:3.11
COPY requirements.txt /
# Встановимо змінну середовища
ENV Personal_assistant /bot_interface

# Встановимо робочу директорію усередині контейнера
WORKDIR $Personal_assistant

# Скопіюємо інші файли до робочої директорії контейнера
COPY . /bot_interface

# Встановимо залежності усередині контейнера
RUN pip install --no-cache-dir -r /requirements.txt

# Позначимо порт де працює програма всередині контейнера
EXPOSE 5000

# Запустимо нашу програму всередині контейнера

ENTRYPOINT ["python", "bot_interface.py"]
