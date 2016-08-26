#!/usr/bin/python
#
#script scans all images in the subdirectories, reads the exif data and export to a json file
#

import json, os, exifread
from glob import glob
from datetime import datetime
from time import mktime

force = True #force rewrite database json

def reformatDtime(dtime):
	dt = datetime.strptime(str(dtime), '%Y:%m:%d %H:%M:%S')
	unix = str(int(mktime(dt.timetuple())*1000))
	return dt.strftime('%Y/%m/%d'), dt.strftime('%H:%M'), unix

def extractExif(fpath):
	""" extract some exif data of the image located at filepath """
		
	with open(fpath, 'r') as f:
		exif = exifread.process_file(f)
		
	date, time, timestamp = reformatDtime(exif['EXIF DateTimeOriginal'])
	baseName, extension = fpath.split('/')[-1][:-4], fpath.split('.')[-1]
	return {'date':date,
			'time':time,
			'timestamp':timestamp,
			'categories':[],
			'name':'',
			'description':'',
			'filename': baseName+'.'+extension,
			'albums':[],
			'thumbnail':baseName+'_thumb.'+extension}

if __name__ == '__main__':
	images = sorted(glob('./*/*.jpg'))
	
	if os.path.exists('database.json'):
		try:
			with open('database.json','r') as f:
				database = json.load(f)
		except Exception, e:
			print 'ERROR loading database json'
			print str(e)
			if raw_input('continue to overwrite database json? type "yes": ').lower() == 'yes':
				database = []
			
	else:
		database = []

	for image in images:
		img_name = image.split('/')[-1][:-4]
		if not img_name in database or force:
			exif = extractExif(image)
			database.append(exif)
			print 'added',img_name,'record'
		else:
			print img_name,'already exists in database, skipping..'
	
	with open('database.json','w') as f:
		json.dump(database, f)
		
