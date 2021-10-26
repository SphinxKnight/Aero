from bs4 import BeautifulSoup
from core.api import c, r, R
import requests
import re


def detail(name, number):
    try:
            n = re.search(r'([a-zA-Z]+)([0-9]+)', number.lower())
            fn = n.group(1)+'-'+n.group(2)
            a = requests.get(f'https://{name.lower().replace(" ", "-")}.flight-status.info/{fn}')
            s = BeautifulSoup(a.text, 'html.parser')
            m = s.findAll('ul', class_='a3_n')
            if a.status_code == 404:
                print(f'[ {R}*{r} ] No additional flight details')
            for data in m[0], m[2], m[3]:
                for j in data.text.split('\n\n'):
                    full = str(j.strip().replace(': ', ' : '))
                    for t in full.split('\n'):
                        var = f'[ {c}*{r} ] ' + t.split(':')[0]
                        ans = c + t.split(':')[1] +r
                        final = var + ':' + ans
                        print(final)

    except:
        print('')
