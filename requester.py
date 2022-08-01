import requests
import json


def get_data(start_date, end_date):
    url = f"https://api.apilayer.com/currency_data/timeframe?start_date={start_date}&end_date={end_date}"
    key = "8nOp4eBHO7jSOj7BylImI0OEPHGaEp4t"
    headers = {"apikey": key}
    response = requests.request(method="GET", url=url, headers=headers)
    if response.status_code == 200:
        print(f"Запрос выполнен успешно. {response.status_code}")
    else:
        print(f"Запрос выполнен не успешно. {response.status_code}")
        exit(400)
    text = response.text
    data = json.loads(text)
    return data['quotes']

if __name__ == '__main__':
    result = {}
    quotes = get_data(start_date='2022-07-01', end_date='2022-08-01')
    print()
