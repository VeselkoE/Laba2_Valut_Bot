"""
Сдесь указан токен и доступная валюта
"""
# MY_TOKEN = '7698137597:AAEC0Hl3EiYt4j1CiSd_kSnJVcJQqcIIUkk'
# all_key = {
#     'Рубль': 'RUB',
#     'Доллар': 'USD',
#     'Евро': 'EUR',
# }
#import chardet
def load_config(filename):
    config = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key] = value
    return config

# Загрузка данных из файла
config = load_config('API_TOKEN.txt')

# Получение токена и валют
MY_TOKEN = config.get('MY_TOKEN')
all_key = {key: value for key, value in config.items() if key != 'MY_TOKEN'}

# Проверка
print("Токен:", MY_TOKEN)
print("Словарь валют:", all_key)