import requests
import json
import time

# Замените '1d' на нужный вам интервал (1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M)
interval = '1d'

# ANYPAIR
symbol = 'ETHUSDT'

# Начальное время в миллисекундах (например, 5 лет назад)
start_time = int((time.time() - 5 * 365 * 24 * 60 * 60) * 1000)

all_data = []

while True:
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&startTime={start_time}&limit=1000'
    response = requests.get(url)
    data = json.loads(response.text)
    if not data:
        break
    all_data.extend(data)
    start_time = data[-1][0] + 1  # Увеличиваем startTime на 1 миллисекунду после последней свечи

# Создаем имя файла с текущим временем, чтобы каждый файл был уникальным
filename = f'data_{time.strftime("%Y%m%d-%H%M%S")}.json'

# Сохраняем все данные в файл JSON в читаемом формате
with open(filename, 'w') as f:
    json.dump(all_data, f, indent=4, sort_keys=True)
