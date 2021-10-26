import time
from modules.aircraft import *
from modules.arrival import *
from modules.departure import *
from modules.flight import *
from modules.status import *
from modules.model import *
from modules.airline import *
from modules.ls import *
try:
    print(f'''{c}                  
                                 |
                                _|_
                               /___{chr(92)}
                              /_____{chr(92)}
                             /oo   oo{chr(92)}
 \___________________________\       /___________________________/
  `-----------|------|--------\_____/--------|------|-----------'
             ( )    ( )     O|OOo|oOO|O     ( )    ( ){r}''')
    print(f'''
[ {c}→{r} ] Options\n
[ {c}1{r} ] Flight details          [ {c}4{r} ] Flight departure        
[ {c}2{r} ] Aircraft details        [ {c}5{r} ] Flight arrival
[ {c}3{r} ] Airline details         [ {c}6{r} ] Flight route\n''')

    print(f'[ {c}?{r} ] Enter {c}Option{r} e.g. {c}1{r} ?\n{c}  →  {r} ', end='')
    opt = input()
    print(f'\n[ {c}?{r} ] Enter {c}Airline Name{r} e.g. {c}American Airlines{r} ?\n{c}  →  {r} ', end='')
    name = input()
    print(f'\n[ {c}?{r} ] Enter {c}Flight Number{r} e.g. {c}AA1004{r} ?\n{c}  →  {r} ', end='')
    number = input()
    print(f'\n[ {c}?{r} ] Enter {c}Flight Date{r} e.g. {c}2021-10-30{r} ?\n{c}  →  {r} ', end='')
    date = input()

    if opt == '1':
        print(f'\n[ {c}#{r} ] Finding flight details\n')
        time.sleep(1)
        other(name, number, date)
        flight(name, number, date)
        detail(name, number)
        print()

    if opt == '2':
        print(f'\n[ {c}#{r} ] Finding aircraft details\n')
        time.sleep(1)
        aircraft(name, number, date)
        print()

    if opt == '6':
        print(f'\n[ {c}#{r} ] Finding flight route\n')
        time.sleep(1)
        duration(name, number, date)
        print()

    if opt == '4':
        print(f'\n[ {c}#{r} ] Finding departure details\n')
        time.sleep(1)
        departure(name, number, date)
        print()

    if opt == '5':
        print(f'\n[ {c}#{r} ] Finding arrival details\n')
        time.sleep(1)
        arrival(name, number, date)
        print()

    if opt == '3':
        print(f'\n[ {c}#{r} ] Finding airline details\n')
        time.sleep(1)
        detaild(name, number)
        print()


except KeyboardInterrupt:
    print(f'[ {R}*{r} ] Ctrl+C pressed\n')

except requests.exceptions:
    print(f'[ {R}*{r} ] No internet\n')

except json.decoder.JSONDecodeError:
    print(f'[ {R}*{r} ] Decode error\n')

except IndexError and TypeError and ValueError and AttributeError:
    print(f'[ {R}*{r} ] Input error\n')
