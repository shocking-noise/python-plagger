"""
example

- module: operators.unique
  config:
    key: '1'
"""

def unique(config,data):
    key = config['key']
    ret_data = {}
    for line in data:
        if key not in ret_data:
            ret_data[line[key]] = line
    return ret_data.values()

