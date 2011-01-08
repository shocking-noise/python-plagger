"""
example

- module: source.fetch_data
  config:
    url: http://...
    path: results

"""

import urllib2
import types
from xml.dom import minidom

import simplejson

TYPE_JSON='application/json'
TYPE_ATOM_XML='application/atom+xml'

def fetch_data(config,data):
    responce = urllib2.urlopen(config['url'])
    responce_type = responce.headers.gettype()
    print responce_type
    
    contents = None
    if responce_type == TYPE_ATOM_XML:
        print 'ATOM'
        contents = xml_to_json(responce.read())
    if responce_type == TYPE_JSON:
        print 'JSON'
        contents = responce.read()

    res = simplejson.loads(contents)
    items = config['path'].split('.')
    tmp = res
    for item in items:
        tmp = tmp[item]
    return tmp


JSON_TEXT_KEY = "#text"
JSON_ATTR_PREFIX = "@"

def xml_to_json(xml_doc):
    doc_el = minidom.parseString(xml_doc).documentElement
    #doc_el = xml_doc.documentElement
    json_doc = {doc_el.nodeName : xml_node_to_json(doc_el)}

    return simplejson.dumps(json_doc)

def xml_node_to_json(xml_node):
    if((len(xml_node.childNodes) == 1) and
       (xml_node.childNodes[0].nodeType == xml_node.TEXT_NODE)):
        if(len(xml_node.attributes) == 0):
            return xml_node.childNodes[0].data
        else:
            json_node = {}
            json_node[JSON_TEXT_KEY] = xml_node.childNodes[0].data            
            xml_node_attrs = xml_node.attributes
            for attr_name in xml_node_attrs.keys():
                json_node[JSON_ATTR_PREFIX + attr_name] = xml_node_attrs[attr_name].nodeValue
            return json_node
    else:
        json_node = {}
        
        for child_xml_node in xml_node.childNodes:
            new_child_json_node = xml_node_to_json(child_xml_node)
            cur_child_json_node = json_node.get(child_xml_node.nodeName, None)
            if(cur_child_json_node is None):
                cur_child_json_node = new_child_json_node
            else:
                # if we have more than one of the same type, turn the children into a list
                if(not isinstance(cur_child_json_node, types.ListType)):
                    cur_child_json_node = [cur_child_json_node]
                cur_child_json_node.append(new_child_json_node)
            json_node[child_xml_node.nodeName] = cur_child_json_node
            
        xml_node_attrs = xml_node.attributes
        #for attr_name in xml_node_attrs.keys():
        #    json_node[JSON_ATTR_PREFIX + attr_name] = xml_node_attrs[attr_name].nodeValue

        return json_node
