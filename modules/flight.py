from .model import *


def flight(name, number, date):

    data = api.get(name, number, date)
    for a_data in data:
        a_info = a_data['flight']
        fnumber = a_info['number']
        iata = a_info['iata']
        icao = a_info['icao']
        print(f'[ {c}*{r} ] Number : {c}{fnumber}{r}')
        print(f'[ {c}*{r} ] IATA : {c}{iata}{r}')
        print(f'[ {c}*{r} ] ICAO : {c}{icao}{r}')
