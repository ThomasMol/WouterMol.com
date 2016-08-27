import json, os

def convert(fname):
	with open(fname,'r') as f:
		database = json.load(f)
	
	if os.path.exists('database/init.csv'):
		print 'warning! init.csv already exists, backup to initOLD.csv'
		os.rename('database/init.csv','database/initOLD.csv')
		
	csv = open('database/init.csv','w')
	order = ['filename','name','categories','albums',
			 'description','location','date','time','thumbnail','timestamp']
	order_ix = {}
	
	header = True
	for entry in database:
		if header:
			names = entry.keys()
			for name in names:
				order_ix[names.index(name)] = order.index(name)
			names.sort(key= lambda x: order.index(x))
			names = ';'.join(names)
			header = False
			csv.write('%s\n'%names)
		
		contents = [entry[i] for i in entry]
		for i in range(len(contents)):
			if type(contents[i]) == list:
				contents[i] = ', '.join(contents[i])
		contents = sorted(contents,key= lambda x: order_ix[contents.index(x)])
		csv.write('%s\n'%(';'.join(contents)))
	
	csv.close()
	
if __name__ == '__main__':
	convert('database/database.json')
	
		

