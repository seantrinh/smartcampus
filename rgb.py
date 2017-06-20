import time
import sys
import datetime

import Adafruit_TCS34725
import smbus
tcs = Adafruit_TCS34725.TCS34725()

import MySQLdb

db = MySQLdb.connect(
    host = '192.168.1.151',
    user = 'pi',
    passwd = '10416232',
    db = 'rgb',
    port = 3306)

curs=db.cursor()

try:
    while True:
        r, g, b, c = tcs.get_raw_data()
        color_temp = Adafruit_TCS34725.calculate_color_temperature(r,g,b)
        lux = Adafruit_TCS34725.calculate_lux(r,g,b)
        print('Color: red={0}, green={1}, blue={2}, clear={3}'.format(r,g,b,c))
        
if color_temp is not None:
            print('Color Temperature: {0} K'.format(color_temp))

        print('Luminosity: {0} lux'.format(lux))
        print('--------------------------------------------------')

        add_rgb = ("INSERT INTO rgb VALUES(%s,%s,%s,%s,%s,%s,%s,%s)")
        curs.execute(add_rgb, (time.strftime("%Y/%m/%d"), time.strftime("%H:%M:%S"), r, g, b, c, color_temp, lux))
        db.commit()

        time.sleep(10)

except KeyboardInterrupt:
    print "\nA keyboard interrupt has been noticed"
    
except:
    print "An error or exception has occurred"
