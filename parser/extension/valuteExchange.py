import xml.etree.ElementTree as ET
from datetime import datetime

import requests
from config import config

previous_date = ''
previous_exchange_rate = ''


def get_curs_value(data_string):
    global previous_date
    global previous_exchange_rate
    date_object = datetime.strptime(data_string, '%Y-%m-%dT%H:%M:%S').date()
    day = date_object.day if date_object.day >= 10 else '0' + str(date_object.day)
    month = date_object.month if date_object.month >= 10 else '0' + str(date_object.month)
    year = date_object.year
    date = f'{day}.{month}.{year}'
    if date != previous_date:
        r = requests.get(f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={date}', timeout=None)
        previous_date = date
        data = r.text
        root = ET.fromstring(data)
        valute = config['valute']
        result = root.find(f'./Valute[CharCode="{valute}"]')
        result = result.find('Value')
        previous_exchange_rate = result.text
        return previous_exchange_rate
    return previous_exchange_rate
