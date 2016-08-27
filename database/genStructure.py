#!/usr/bin/python
#
#generate a structure files filled with all categories/themes/albums/locations
#based on database.json

import json

with open('database/database.json', 'r') as f:
    database = json.load(f)

attributes = ['albums','categories','location']

for attrib in attributes:
    print attrib
    values = []
    for image in database:
        contents = image[attrib]
        if type(contents) == list:
            for value in contents:
                if len(value) > 0 and value not in values:
                    values.append(value)
        elif type(contents) == str:
            if contents not in values:
                values.append(contents)
    if 'loc' in attrib:
        attrib += 's'
    with open('database/%s.json'%attrib,'w') as f:
        json.dump(values, f)
        
