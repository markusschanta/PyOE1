import datetime
import pandas as pd
import requests
import argparse
import sys

BASE_URL = 'http://oe1.orf.at/programm/konsole/tag/'

DEFAULT_COLUMNS = ['time', 'title', 'info']

def get_oe1_program(date='20160423', offline=False):
    if offline:
        return _get_oe1_program_offline()
    try:
        url = BASE_URL + str(date)
        response = requests.get(url, stream=True)
        return pd.DataFrame(response.json()['list'])
    except KeyError:
        sys.exit("Can not retreive program for date %s." % date)
    except requests.exceptions.ConnectionError:
        sys.exit("Can not retreive program due to a network error.")

def _get_oe1_program_offline():
    return pd.DataFrame.from_csv('offline.csv', encoding='utf-8')

def post_process_program(program):
    program = program.set_index('id')
    program['datetime'] = program.apply(_get_date_from_row, axis=1)
    return program

def _get_date_from_row(row):
    return datetime.datetime.strptime(row['day_label'] + row['time'], '%d.%m.%Y%H:%M')

def filter_and_print_program(program, args, columns=None):
    # Filter rows to be printed based on command line argument
    if args.filter:
        program = program[program['title'].str.contains(args.filter)]

    # Print title
    title = 'Program for ' + str(args.date)
    if args.filter:
        title += ' (filter: %s)' % args.filter
    title += ':\n'
    print title

    # Filter columns to be printed
    if not columns:
        columns = DEFAULT_COLUMNS
    program = program.loc[:,columns]

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
    filter_and_print_program(program, args=args)

main()
