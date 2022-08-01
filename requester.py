import requests
import json


def get_data(start_date, end_date):  # Мы получаем обе стороны даты
    url = f"https://api.apilayer.com/currency_data/timeframe?start_date={start_date}&end_date={end_date}" # Получение ссылки
    key = "8nOp4eBHO7jSOj7BylImI0OEPHGaEp4t" # Ссылка в ключе
    headers = {"apikey": key} # Переменая в которой есть два ключа, что в будующем нам помогут
    response = requests.request(method="GET", url=url, headers=headers) # Три ключа, что сидят в респонсе
    if response.status_code == 200: # Проверка, успешный ли код
        print(f"Запрос выполнен успешно. {response.status_code}") # Сообщение о успешной операции
    else: # Если код не успешный
        print(f"Запрос выполнен не успешно. {response.status_code}") # Сообщение о не успешной операции
        exit(400) # Выход из программы из-за того что программа не успешна
    text = response.text # Переменная, хранящая в себе статус программы
    data = json.loads(text) # Использование библиотеку json
    return data['quotes'] # ...

if __name__ == '__main__': # Быстрый запуск
    result = {} # ...
    quotes = get_data(start_date='2022-07-01', end_date='2022-08-01') # Конечная проверка даты
    print()
