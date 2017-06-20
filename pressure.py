import Adafruit_BMP.BMP085 as BMP085
import time

sensor = BMP085.BMP085()

##import MySQLdb
##db = MySQLdb.connect("localhost","root","smartcampus","pressure")
##curs = db.cursor()


try:
    while True:

        temp = sensor.read_temperature()
        pressure = sensor.read_pressure()
        altitude = sensor.read_altitude()
        sealevelpressure = sensor.read_sealevel_pressure()

        print('Temp = {0:0.2f} *C'.format(temp))
        print('Pressure = {0:0.2f} Pa'.format(pressure))
        print('Altitude = {0:0.2f} m'.format(altitude))
        print('Sealevel Pressure = {0:0.2f} Pa'.format(sealevelpressure))
        print('------------------------------------------')

##        add_pressure = ("INSERT INTO pressurerecord VALUES(%s,%s,%s,%s,%s,%s)")
##        curs.execute(add_pressure, (time.strftime("%Y/%m,%d"), time.strftime("%H:%M:%S"),temp, pressure, altitude, sealevelpressure))              
##        db.commit()
##        time.sleep(10)
        time.sleep(10)


except KeyboardInterrupt:
    print "\nA keyboard interrupt has been noticed"

except:
    print "An error or exception has occurred"

