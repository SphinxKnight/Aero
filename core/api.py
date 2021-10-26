import colorama
from colorama import Fore, Style
import requests
import json

colorama.init()

c = Fore.LIGHTYELLOW_EX
r = Style.RESET_ALL
R = Fore.RED


def get(name, number, date):

    try:
        url = f'https://aviationstack.com/flight_api.php?airline={name}&flight_number={number}&flight_date={date}'
        data = requests.get(url).text
        info = json.loads(data)['data']
        return info
    except:
        return ''