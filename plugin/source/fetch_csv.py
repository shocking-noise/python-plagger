"""
example

- module: source.fetch_csv
  config:
    path: /usr/...
    skip_rows: 0
    column_name: 0
"""

import csv

def fetch_csv(config,data):
    skip_rows = config.get('skip_rows') or 0
    column_name = config.get('column_name') or 0
    header = []
    for i,row in  enumerate(csv.reader(open(config['path'],'r'))):
        if column_name == i:
            for element in row :
                header.append(element)
        if i > skip_rows :
            line = {}
            for i,element in enumerate(row):
                line[header[i]] = element
            data.append(line)
    return data

