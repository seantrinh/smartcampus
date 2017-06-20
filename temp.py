import time
import sys
import datetime
#import Adafruit_BMP.BMP085 as BMP085
#import Adafruit_DHT

import MySQLdb

#sensor = BMP085.BMP085()
#sensor2 = Adafruit_DHT.DHT22
#pin = 24

db = MySQLdb.connect(
    host = '192.168.1.151',
    user = 'pi',
    passwd = '10416232',
    db = 'temp',
    port = 3306)

curs=db.cursor()


try:
    while True:
        #---------------------------------------------------------------------------------------
        #Waterproof Temperature Sensor
	tfile = open("/sys/bus/w1/devices/28-00000608f21c/w1_slave")
        text = tfile.read()
        tfile.close()

        secondLine = text.split("\n")[1]

        temperaturedata = secondLine.split(" ")[9]

        temperature = float(temperaturedata[2:])
        temp = (temperature/1000.0) * (9/5) + 32

        print (temp, 'A')

        add_temp = ("INSERT INTO temprecord VALUES(%s, %s, %s, %s)")
	curs.execute(add_temp, (temp, 'A', time.strftime("%Y/%m/%d"), time.strftime("%H:%M:%S")))
        db.commit()
	
	#-----------------------------------------------------------------------------------------
        #Barometric Pressure Sensor
##        temp2 = sensor.read_temperature() * (9/5) + 32
##        print (temp2, 'B')
##        curs.execute(add_temp, (temp2, 'B', time.strftime("%Y/%m/%d"), time.strftime("%H:%M:%S")))
##        db.commit()

        #-----------------------------------------------------------------------------------------
        #DHT11 Temperature/Humidity Sensor
##        humidity, temp3 = Adafruit_DHT.read_retry(sensor2, pin)
##        temperature3 = temp3 / 10 
##        print(temperature3, humidity, 'C')
##
##        curs.execute(add_temp, (temperature3, 'C', time.strftime("%Y/%m/%d"), time.strftime("%H:%M:%S")))
##        db.commit()


##        #--------------------------------------------------------------------------------------
##
##        tfile2 = open("/sys/bus/w1/devices/28-0000060882e5/w1_slave")
##        text2 = tfile2.read()
##        tfile2.close()
##
##        secondLine2 = text2.split("\n")[1]
##
##        temperaturedata2 = secondLine2.split(" ")[9]
##
##        temperature2 = float(temperaturedata2[2:])
##        temp2 = (temperature2/1000.0) * (9/5) + 32
##
##        print (temp2, 2)
##
##        add_temp2 = ("INSERT INTO temprecord VALUES(%s, %s, %s, %s)")
##
##        curs.execute(add_temp2, (temp2, 'B', time.strftime("%Y/%m/%d"), time.strftime("%H:%M:%S")))
##        db.commit()

        time.sleep(900)#900

except KeyboardInterrupt:
    print "\nA keyboard interrupt has been noticed"

except:
    print "An error or exception has occurred."
	
