from bs4 import BeautifulSoup
from core.api import c, r, R
import requests
import re


def detaild(name, number):
            n = re.search(r'([a-zA-Z]+)([0-9]+)', number.lower())
            fn = n.group(1)+'-'+n.group(2)
            a = requests.get(f'https://{name.lower().replace(" ", "-")}.flight-status.info/{fn}')
            s = BeautifulSoup(a.text, 'html.parser')
            m = s.findAll('ul', class_='a3_n')
            if a.status_code == 404:
                print(f'[ {R}*{r} ] No additional airline details')
            k = m[1].text.replace(': ', ' : ').strip().split('\n')
            print(f'[ {c}*{r} ] Name : {c}{str(k[0])}{r}')
            print(f'[ {c}*{r} ] IATA : {c}{str(k[1].split(":")[1].strip())}{r}')
            print(f'[ {c}*{r} ] ICAO : {c}{str(k[2].split(":")[1].strip())}{r}')
            print(f'[ {c}*{r} ] Operating Days : {c}{str(k[3].split(":")[1].strip())}{r}')

