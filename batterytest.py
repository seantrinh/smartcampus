import time
time.sleep(10)
import sys

import MySQLdb

db = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='smartcampus',
        db='batterytest')

curs=db.cursor()
#counter=0
try:
        curs.execute('SELECT * FROM batterytest')
        data = curs.fetchall()
        if str(data[0]) == '(0L,)':
                while True:
                        time.sleep(10)
                        updateCounter = ("UPDATE batterytest SET c = c + 1")
                        curs.execute(updateCounter)
                        db.commit()
                        print("Counter updated")
        else:
                print("Test complete")
except KeyboardInterrupt:
        print "\nA keyboard interrupt has been noticed"

except:
        print "An error or exception occurred"
        
#Remember to configure the Raspberry Pi to start this script at startup
