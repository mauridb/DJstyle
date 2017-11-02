# 41.40338, 2.17403
import os, sys, shutil
import random
import csv

from termcolor import colored as c
from datetime import datetime as dt 

args = sys.argv
filename = sys.argv[2]
try:
	input_times = int(args[1])
	print c('OK: Input cust to integer..', 'green')

except Exception as e:
	# print e
	print c('KO: Insert an int value..', 'red')


points = [ {'ID':'pnt{}'.format(index),'lat':round(random.uniform(-70.0,70.0),6),'lng':round(random.uniform(-160.0,160.0),6)} for index in range(0,input_times)]
# print points

if os.path.exists('data/')==True:
	print c('INFO: Folder already exists', 'yellow')
else:
	os.system("mkdir data")
	print c('OK: Created folder data','green')

os.system("touch data/{}.csv".format(filename))
print c('OK: Created dataset.csv file','green')

with open("data/{}.csv".format(filename), 'w') as csvfile:
    fieldnames = ['POINT', 'LAT', 'LNG']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in points:
    	writer.writerow({'POINT': i['ID'], 'LAT': i['lat'],'LNG':i['lng']})

print c('OK: Cool, your dataset is ready to parse.. Enjoy<3!','green')
