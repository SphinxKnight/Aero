import requests
from core import api
from core.api import c, r, R
from bs4 import BeautifulSoup


def aircraft(name, number, date):

    data = api.get(name, number, date)
    for a_data in data:
        try:
            a_info = a_data['aircraft']
            register = a_info['registration']
            iata = a_info['iata']
            icao = a_info['icao']
            icao24 = a_info['icao24']
            print(f'[ {c}*{r} ] Registration Number : {c}{str(register)}{r}')
            print(f'[ {c}*{r} ] IATA Code : {c}{str(iata)}{r}')
            print(f'[ {c}*{r} ] ICAO Code : {c}{str(icao)}{r}')
            print(f'[ {c}*{r} ] ICAO24 Code : {c}{str(icao24)}{r}')
            add = requests.post('http://rzjets.net/aircraft/', {
                'registry': register,
                'submitB': 'search'
            }).text
            soup = BeautifulSoup(add, 'html.parser')
            mod = soup.findAll('td', class_='current')[0].text
            engine = soup.findAll('td', class_='currentnw')[2].text
            print(f'[ {c}*{r} ] Model : {c}{mod}{r}')
            print(f'[ {c}*{r} ] Engine : {c}{engine}{r}')
        except:
            print(f'[ {R}*{r} ] No Data')

