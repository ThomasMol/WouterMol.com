#!/usr/bin/python
#
#generate a structure files filled with all categories/themes/albums/locations
#based on database.json

import json,os,time
   
#load main database file
with open('database.json', 'r') as f:
    database = json.load(f)

#the attributes that need seperate files
attributes = ['albums','categories','location']

#generate dir structure
for attrib in attributes:
    if not os.path.exists('./%s'%attrib):
        os.makedirs('./%s'%attrib)

#generate the seperate database files per attribute
for attrib in attributes:
    timeStart = time.time()
    values = []
    for image in database:
        contents = image[attrib]
        if type(contents) == list:
            for value in contents:
                if len(value) > 0 and value not in values:
                    values.append(value)
        elif type(contents) == unicode:
            if contents not in values:
                values.append(contents)
        else:
            print 'error', type(contents)
    
    for value in values:
        #append to existing database if it exists
        if os.path.exists('%s/%s.json'%(attrib, value)):
            with open('%s/%s.json'%(attrib, value)) as f:
                match = json.load(f)
        else:
            match = []
        
        entries = [i['filename'] for i in match]
        for image in database:
            if value in image[attrib]:
                if image['filename'] not in entries:
                    print 'adding %s to %s'%(image['filename'], value)
                    match.append(image)
        
        with open('%s/%s.json'%(attrib,value),'w') as f:
            json.dump(match, f)
    
    timeEnd = time.time()
    print 'generation of %s files took %.4f seconds'%(attrib, timeEnd-timeStart)
        
