import datetime
import pandas as pd
import requests
import argparse

BASE_URL = 'http://oe1.orf.at/programm/konsole/tag/'

DEFAULT_COLUMNS = ['time', 'title', 'info']

def get_oe1_program(date='20160423', offline=False):
    if offline:
        return _get_oe1_program_offline()
    url = BASE_URL + str(date)
    response = requests.get(url, stream=True)
    return pd.DataFrame(response.json()['list'])

def _get_oe1_program_offline():
    return pd.DataFrame.from_csv('offline.csv', encoding='utf-8')

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

def print_program(program, date=None):
    if date:
        print 'Program for ' + str(date) + ':\n'
    program.columns = [c.title() for c in program.columns]
    print program.to_string(index=False).encode('utf-8')

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--date", help="Date for which to obtain program items for", type=int, default=0)
    parser.add_argument("-f", "--filter", help="String to filter program elements by", type=str)
    parser.add_argument("-u", "--url", help="Print URL(s) of matching program items only", action="store_true")

    args = parser.parse_args()

    if args.date <= 0:
        args.date = (datetime.datetime.today() + datetime.timedelta(days=args.date)).strftime("%Y%m%d")

    return args

def main():
    args = parse_args()

    program = get_oe1_program(date=args.date)
    program = filter_program(post_process_program(program))

    print_program(program, date=args.date)

main()

#print_program(filter_program(post_process_program(get_oe1_program(offline=True))))
