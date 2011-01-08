"""
example

- module: source.union
  config:
    - module: ...
    - moeule: ...
"""

def union(config,data):
    data2 = eval_pyplagger(config,[])
    return data + data2
