from core import api
from core.api import c, r


def other(name, number, date):

    data = api.get(name, number, date)
    for a_data in data:
        status = a_data['flight_status']
        live = a_data['live']
        print(f'[ {c}*{r} ] Status : {c}{str(status)}{r}')
        print(f'[ {c}*{r} ] Live : {c}{str(live)}{r}')
