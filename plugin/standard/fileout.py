"""
example

- module: standard.fileout
  config: 
    path: /usr/...
"""

def fileout(config,data):
    out = open(config['path'],'w')
    out.write('\n'.join(data))
    out.close()
    return data
