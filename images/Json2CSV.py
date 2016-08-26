import json


def convert(fname):
	with open(fname,'r') as f:
		database = json.load(f)
		
	csv = open('database.csv','w')
	
	header = True
	
	for entry in database:
		if header:
			names = ';'.join(entry.keys())
			header = False
			csv.write('%s\n'%names)
		
		contents = [entry[i] for i in entry]
		for i in range(len(contents)):
			if type(contents[i]) == list:
				contents[i] = ', '.join(contents[i])
		#print contents
		csv.write('%s\n'%(';'.join(contents)))
	
	csv.close()

convert('database.json')
		

