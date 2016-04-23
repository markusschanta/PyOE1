@@ -0,0 +1,27 @@
import datetime
import pandas as pd
import requests

BASE_URL = 'http://oe1.orf.at/programm/konsole/tag/'

DEFAULT_COLUMNS = ['time', 'title', 'info']

def get_oe1_program(day='20160423'):
    url = BASE_URL + day
    response = requests.get(url, stream=True)
    return pd.DataFrame(response.json()['list'])

def _get_date_from_row(row):
    return datetime.datetime.strptime(row['day_label'] + row['time'], '%d.%m.%Y%H:%M')

def post_process_program(program):
    program = program.set_index('id')
    program['datetime'] = program.apply(_get_date_from_row, axis=1)
    return program

def filter_program(program, columns=None):
    if not columns:
        columns = DEFAULT_COLUMNS
    return program.loc[:,columns]

print get_oe1_program()
