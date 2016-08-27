import json, os

def convert(fname):
    csv = open(fname,'r').read().split('\n')
    database = []
    plural = ['albums','categories']
    
    header = True
    for line in csv[:-1]:
        if header:
            keys = line.split(';')
            header = False
        else:
            contents = line.split(';')
            item = {}
            for i in range(len(keys)):
                if keys[i] in plural:
                    item[keys[i]] = contents[i].split(', ')
                else:
                    item[keys[i]] = contents[i]
            database.append(item)
    
    if os.path.exists('database/database.json'):
        print 'Warning! database already exists, saving backup to databaseOLD.json'
        os.rename('database/database.json','database/databaseOLD.json')
    
    with open('database/database.json','w') as f:
        json.dump(database, f)
    
                
        

if __name__ == '__main__':
    convert('database/init.csv')
