from core import api
from core.api import c, r


def departure(name, number, date):

    data = api.get(name, number, date)
    for a_data in data:
        a_info = a_data['departure']
        airport = a_info['airport']
        timezone = a_info['timezone']
        iata = a_info['iata']
        icao = a_info['icao']
        terminal = a_info['terminal']
        gate = a_info['gate']
        delay = a_info['delay']
        scheduled = a_info['scheduled']
        estimated = a_info['estimated']
        actual = a_info['actual']
        estimated_runway = a_info['estimated_runway']
        actual_runway = a_info['actual_runway']
        print(f'[ {c}*{r} ] Airport Name : {c}{str(airport)}{r}')
        print(f'[ {c}*{r} ] Timezone : {c}{str(timezone)}{r}')
        print(f'[ {c}*{r} ] IATA Code : {c}{str(iata)}{r}')
        print(f'[ {c}*{r} ] ICA0 Code : {c}{str(icao)}{r}')
        print(f'[ {c}*{r} ] Terminal : {c}{str(terminal)}{r}')
        print(f'[ {c}*{r} ] Gate : {c}{str(gate)}{r}')
        print(f'[ {c}*{r} ] Delay : {c}{str(delay)}{r}')
        print(f'[ {c}*{r} ] Scheduled Time : {c}{str(scheduled)}{r}')
        print(f'[ {c}*{r} ] Estimated Time : {c}{str(estimated)}{r}')
        print(f'[ {c}*{r} ] Actual Time : {c}{str(actual)}{r}')
        print(f'[ {c}*{r} ] Estimated Runway Time : {c}{str(estimated_runway)}{r}')
        print(f'[ {c}*{r} ] Actual Runway Time : {c}{str(actual_runway)}{r}')