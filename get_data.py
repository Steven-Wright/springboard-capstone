import requests
import argparse
from datetime import date
import json

def get_params(date, limit=1000, offset=0):
    params = ["$limit={0}".format(limit), "$where=created_date > '{0}T00:00:00'".format(date)]

    if offset > 0:
        params.insert(1, "$offset={0}".format(offset))

    return "?" + "&".join(params)
  
# Default values
CHUNK_SIZE = 128 * 1024
BULK_FILENAME = '311_Service_Requests_from_2010_to_Present.csv'
BULK_ENDPOINT = 'https://data.cityofnewyork.us/api/views/erm2-nwe9/rows.csv?accessType=DOWNLOAD'
SINCE_FILENAME = '311_Service_Requests.json'
SINCE_ENDPOINT = 'https://data.cityofnewyork.us/resource/erm2-nwe9.json'
SINCE_LIMIT = 1000

# Command line interface
parser = argparse.ArgumentParser(description='collect 311 service request data')
subparsers = parser.add_subparsers(dest='command')
subparsers.required = True

bulk = subparsers.add_parser('bulk')
bulk.add_argument('--file', '-f', default=BULK_FILENAME)
bulk.add_argument('--chunk_size', '-bs', default=CHUNK_SIZE)
bulk.add_argument('--url', default=BULK_ENDPOINT)

day = subparsers.add_parser('since')
day.add_argument('--file', '-f', default=SINCE_FILENAME)
day.add_argument('--url', default=SINCE_ENDPOINT)
day.add_argument('day')

args = parser.parse_args()

if args.command == 'bulk':
    # Download all available data as csv
    r = requests.get(args.url, stream=True)

    with open(args.file, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=args.chunk_size):
            fd.write(chunk)

if args.command == 'since':
    # Download data from JSON API since date
    try:
        date.fromisoformat(args.day)
    except ValueError:
        print("Unable to parse provided date, exiting...")
        exit

    # Warning - will load all data into memory
    r = requests.get(args.url + get_params(args.day, SINCE_LIMIT))
    data = r.json()
    new_records = len(data)
    while new_records == SINCE_LIMIT:
        r = requests.get(args.url + get_params(args.day, SINCE_LIMIT, len(data)))
        new_data = r.json()
        new_records = len(new_data)
        data.extend(new_data)

    with open(args.file, 'w') as fd:
        fd.write(json.dumps(data))
    