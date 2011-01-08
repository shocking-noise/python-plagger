"""
example

- module: operators.truncate
  config:
    n: 5
"""

def truncate(config,data):
    return data[0:config['n']]
