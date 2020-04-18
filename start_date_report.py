#!/usr/bin/env python3
import csv
import datetime
import requests
import io
from collections import defaultdict

FILE_URL="http://marga.com.ar/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()
    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url)
    response.encoding = 'utf-8'
    # Decode all lines into strings
    csvio = io.StringIO(response.text, newline="")
    return csvio




def get_same_or_newer(start_date):
    """Returns the employees that started on the given date, or the closest one."""
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data)
    result = defaultdict(list)
    result = defaultdict(list)
    for row in reader:
        key = row[3]
        result[key].append("{} {}".format(row[0], row[1]))

    for k, v in sorted(result.items()):
        row_date = datetime.datetime.strptime(k, '%Y-%m-%d')
        if row_date < start_date:
            continue
        if row_date > datetime.datetime.today():
            print("Started on {}: {}".format(datetime.datetime.today().strftime("%b %d, %Y"), []))
            break
        t = datetime.datetime.strptime(k, '%Y-%m-%d')
        print("Started on {}: {}".format(t.strftime("%b %d, %Y"), v))

def main():
    start_date = get_start_date()
    get_same_or_newer(start_date)
if __name__ == "__main__":
    main()






