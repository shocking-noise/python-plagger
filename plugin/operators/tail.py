"""
example

- module: operators.tail
  config:
    n: 5
"""

def tail(config,data):
    size = len(data)
    return data[size - config['n']:size]
