import requests


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
    print()

# url = "https://api.apilayer.com/currency_data/timeframe?start_date=2022-01-08&end_date=2022-04-0310"
#
# payload = {}
# headers= {
#   "apikey": "8nOp4eBHO7jSOj7BylImI0OEPHGaEp4t"
# }
# response = requests.request("GET", url, headers=headers, data = payload)
#
# status_code = response.status_code
# result = response.text
if __name__ == '__main__':
    result = {}
    get_data(start_date='2022-01-08', end_date='2022-04-03')
    print()
