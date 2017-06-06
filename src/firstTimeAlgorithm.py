'''
Created on Jun 6, 2017

@author: Kyle Wong
Created from archived file
First run at just adding the time parameter to our algorithm
Changing the fetch time
'''

import time
import psycopg2
start = time.time()
conn = psycopg2.connect(dbname = 'postgres', host= 'localhost', port= 5432, user = 'postgres',password= 'dragon01')
cur = conn.cursor()

# Our test data
# The main bulk of our test
testintersect = '''select a.gid,b.gid,ST_Intersects(a.geom, b.geom),a.point, a.time, b.polygon, b.time, ST_asTEXT(a.geom)
from testpointtime a, testpolytime b '''



projintersect = '''select a.pid,b.pyid,ST_Intersects(a.geom, b.geom)
from points500 a, poly10 b '''
cur.execute(testintersect)
conn.commit()
cur.execute(testintersect)
parseArray = cur.fetchall()

#print(parseArray)
container = list()
print(parseArray[2])
first = parseArray[2]
#Main loop for actually just parsing the data into a readable format parsing the data
# Just added time to the the parsed info
f = open("C:\Data\ProjectOutputFirstTimeAlgo.txt","w+")
counter = 0
for n in range(len(parseArray)):
    holder = parseArray[n]
    if holder[2] == True:
        ##print(holder[2])
        counter = counter + 1
        writeline = str(holder[3])+"-"+str(holder[4]) +":" + str(holder[5]) +"-"+str(holder[6]) + "\n"
        f.write(writeline)
        container.append(str(holder[3])+"-"+str(holder[4]) +":" + str(holder[5]) +"-"+str(holder[6]))
    
    

print(counter)
end = time.time()

print(end- start)
f.close()
