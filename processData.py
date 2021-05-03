from .models import *
import os


def push_to_db(data):
    try:
        DEFdata1 = DEFdata(instance = data['instance'],
                            master = data['master'],
                            location_x = data['location_x'],
                            location_y = data['location_y'])
        DEFdata1.add()
    except Exception as e:
            print("Error occured while pushing data to DB : {}".format(str(e)))
    else:
        print("Data pushed successfully to DB")

def process_file():
    path = os.path.join(os.getcwd(),'files', 'dhm.comp.txt')
    dict = {}
    try:
        with open(path, 'r') as f:
            for line in f:
                if 'COMPONENT' in line and 'COMPONENTPIN' not in line:                
                    for line in f: # now you are at the lines you want
                        data= line.split(' ')
                        if data[1]=='-':
                            dict['instance'] = data[2]
                            dict['master'] = data[3]
                            if data[7].isnumeric():
                                dict['location_x'] = int(data[7])/1000
                                dict['location_y'] = int(data[8])/1000
                            else:
                                dict['location_x'] = int(data[10])/1000
                                dict['location_y'] = int(data[11])/1000    
                        push_to_db(dict)
    except Exception as e:
        print(dict)
        print(e)

try:
    process_file()
    print("Done")
except Exception as e:
    print("Failed to process the file")