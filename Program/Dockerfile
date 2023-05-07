FROM python:3.11-slim

# Встановлення необхідних пакетів для Tkinter та X11
RUN apt-get update && apt-get install -y \
    python3-tk \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Копіювання та установка залежностей
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

# Копіювання коду програми
COPY . /app
WORKDIR /app

# Запуск програми з Xvfb
CMD ["xvfb-run", "--server-num=1", "--auto-servernum", "python", "bot_interface.py"]
