"""
example

- module: operators.filter
  config:
    regex: ".*"
    key: "key"
    invert: True
"""    
import re

def filter(config,data):
    key = config['key']
    if config.get('invert') is None or config['invert'] == False:
        return [element for element in data if re.match(config['regex'],element[key])]
    else:
        return [element for element in data if not re.match(config['regex'],element[key])]
