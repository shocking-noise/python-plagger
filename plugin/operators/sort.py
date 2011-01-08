"""
example

- module: operators.sort
  config:
    key: "1"
    reverse: False
"""

import operator

def sort(config,data):
    key = config['key']
    reverse = config.get('reverse') or False
    data.sort(key=operator.itemgetter(key),reverse=reverse)
    return data
