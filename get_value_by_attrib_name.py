#!/usr/bin/python3

import sys
from json import loads

def get_value_by_attrib_name(json, attribute_name):
    ihub_data = loads(json)
    return ihub_data[attribute_name]

print(get_value_by_attrib_name(sys.argv[1], sys.argv[2]))