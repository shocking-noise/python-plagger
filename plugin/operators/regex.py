"""
example

- module: operators.regex
  config:
    key: "title"
    pattern: ".*"
    replace: test

"""

import re

def regex(config,data):
    for line in data:
        line[config['key']] = re.sub(config['pattern'],config['replace'],line[config['key']])
    return data

