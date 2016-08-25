#!/usr/bin/python
#
#script scans all images in the subdirectories, reads the exif data and export to a json file
#

import json, os, exifread
from glob import glob
from datetime import datetime

force = True #force rewrite database json

def reformatDtime(dtime):
	dt = datetime.strptime(str(dtime), '%Y:%m:%d %H:%M:%S')
	return dt.strftime('%Y/%m/%d %H:%M')

def extractExif(fpath):
	""" extract some exif data of the image located at filepath """
		
	with open(image, 'r') as f:
		exif = exifread.process_file(f)
		
	dtime = reformatDtime(exif['EXIF DateTimeOriginal'])
	return {'dt':dtime,
			'category':'',
			'name':'',
			'description':''}
	
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
				database = {}
			
	else:
		database = {}

	for image in images:
		img_name = image.split('/')[-1][:-4]
		if not img_name in database or force:
			exif = extractExif(image)
			database[img_name] = exif
			print 'added',img_name,'record'
		else:
			print img_name,'already exists in database, skipping..'
	
	with open('database.json','w') as f:
		json.dump(database, f)
		
