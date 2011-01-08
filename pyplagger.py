import os
import sys
import imp
import re
import optparse

#from pudb import set_trace; set_trace()

rootdir = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(rootdir, "lib"))

import yaml

__version__ = '1.00'

plugins = {}

def dynamic_import(name):
    mod = __import__(name,globals(),locals().[],-1)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod,comp)
    return mod

def load_module(module_name,basedir):
    file,pathname,description=imp.find_module(module_name,[basedir])
    return imp.load_module(module_name,file,pathname,description)

def load_plugins():
    directory = os.path.dirname(__file__) + 'plugin'
    for (root,dirs,files) in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                plugin_path = os.path.join(root, file)
                key = re.sub('^plugin\.','',plugin_path.replace('/','.').replace('.py',''))
                plugins[key] = load_module(file.replace('.py',''),root)

def eval_pyplagger(command_array,data):
    for command in command_array:
        print '=================='
        print command
        print '=================='
        method = getattr(plugins[command['module']],re.sub('^.*\.','',command['module']))
        data = method(command.get('config'),data)

if __name__ == "__main__":
    load_plugins()
    parser = optparse.OptionParser(version="ver:%s" % __version__)
    parser.add_option('-c', '--configure CONFIGFILE', dest = 'configure')
    parser.add_option('-l', '--listplugin', action='store_true', default=False, dest='listplugin')
    (opts, args) = parser.parse_args()
    config = './setting.yaml'
    if opts.listplugin:
        for plugin in  plugins:
            print plugin
        exit(2)
    if opts.configure:
        config = opts.configure
    eval_pyplagger(yaml.load(open(config).read().decode('utf-8')),[])
