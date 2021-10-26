from core import api
from core.api import *


def duration(name, number, date):
    try:
        data0 = api.get(name, number, date)
        for a_data in data0:
            a_info = a_data['arrival']
            airport = a_info['airport']
            data = api.get(name, number, date)
            for a_data in data:
                a_info = a_data['departure']
                airport0 = a_info['airport']
                print(f'[ {c}*{r} ] From : {c}{airport0}{r}')
                p = requests.get(f'https://api.opencagedata.com/geocode/v1/json?q={airport0}&key=03c48dae07364cabb7f121d8c1519492&no_annotations=1&language=en').text
                import json
                dp = json.loads(p)
                for key, value in dp['results'][0]['geometry'].items():
                    print(f'[ {c}*{r} ] {key.replace("lat", "latitude").replace("lng", "longitude")} : {c}{str(value)}{r}')
                print(f'[ {c}*{r} ] Destination : {c}{airport}{r}')
                px = requests.get(f'https://api.opencagedata.com/geocode/v1/json?q={airport}&key=03c48dae07364cabb7f121d8c1519492&no_annotations=1&language=en').text
                dpx = json.loads(px)
                for key, value in dpx['results'][0]['geometry'].items():
                    print(f'[ {c}*{r} ] {key.replace("lat", "latitude").replace("lng", "longitude")} : {c}{str(value)}{r}')
    except:
        print('')

