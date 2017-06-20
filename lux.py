from tsl2561 import TSL2561
import time
import sys
import datetime

import MySQLdb

db = MySQLdb.connect(
    host = '192.168.1.151',
    user = 'pi',
    passwd = '10416232',
    db = 'lux',
    port = 3306)

curs=db.cursor()

try:
    while True:
        tsl = TSL2561(debug=1)
        reading = tsl.lux()
        print(reading)

        add_lux = ("INSERT INTO luxrecord VALUES (%s,%s,%s)")
        curs.execute(add_lux, (time.strftime("%Y/%m/%d"), time.strftime("%H:%M:%S"), reading))
        db.commit()
        time.sleep(10)
        
except KeyboardInterrupt:
    print "\nA keyboard interrupt has been noticed."

except:
    print "An error or exception has occurred."
