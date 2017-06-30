import time
import sys
import datetime

import Adafruit_TCS34725
import smbus
tcs = Adafruit_TCS34725.TCS34725()

import Adafruit_BMP.BMP085 as BMP085
sensor = BMP085.BMP085()

import SI1145.SI1145 as SI1145
sensor_uv = SI1145.SI1145()

#import Adafruit_DHT
#sensor_hum = Adafruit_DHT.DHT22
#pin = 12 #This changes depending on what GPIO port you put it in

import MySQLdb

db = MySQLdb.connect (
  host = 'danube.stevens.edu',
  user = 'pi', #This changes for every sensor suite
  passwd = '10416232', #This also changes for every sensor suite
  db = 'smartcampus',
  port = 3306)

curs=db.cursor()

try:
  while True:
    #RGB SENSOR
    r, g, b, c = tcs.get_raw_data()
    color_temp = Adafruit_TCS34725.calculate_color_temperature(r,g,b)
    lux = Adafruit_TCS34725.calculate_lux(r,g,b)
    print('Color: red={0}, green={1}, blue={2}, clear={3}'.format(r,g,b,c))
    
    if color_temp is not None:
      print('Color Temperature: {0} K'.format(color_temp))
      
    print('Luminosity: {0} lux'.format(lux))
    print('----------------------------------------------------------------')
    
    add_rgb = ("INSERT INTO rgb VALUES(%s,%s,%s,%s,%s,%s,%s,%s)")
    curs.execute(add_rgb, (time.strftime("%Y/%m/%d"), time.strftime("%H:%M:%S"), r, g, b, c, color_temp, lux))
    db.commit()
    
    #PRESSURE SENSOR
    temp = sensor.read_temperature()
    pressure = sensor.read_pressure()
    #altitude = sensor.read_altitude()
    sealevelpressure = sensor.read_sealevel_pressure()
    
    print('Temp = {0:0.2f} *C'.format(temp))
    print('Pressure = {0:0.2f} Pa'.format(pressure))
    #print('Altitude = {0:0.2f} m'.format(altitude))
    print('Sealevel Pressure = {0:0.2f} Pa'.format(sealevelpressure))
    print('----------------------------------------------------------------')
    
    add_pressure = ("INSERT INTO pressurerecord VALUES(%s,%s,%s,%s,%s)")
    curs.execute(add_pressure, (time.strftime("%Y/%m/%d"), time.strftime("%H:%M:%S"), temp, pressure, sealevelpressure))
    db.commit()
    
    #UV SENSOR
    vis = sensor_uv.readVisible()
    IR = sensor_uv.readIR()
    UV = sensor_uv.readUV()
    uvIndex = UV / 100.0
    
    print 'Vis: ' + str(vis)
    print 'IR: ' + str(IR)
    print 'UV Index: ' + str(uvIndex)
    print('----------------------------------------------------------------')
    
    addLight = ("INSERT INTO uvlight VALUES(%s,%s,%s,%s,%s)")
    curs.execute(addLight, (time.strftime("%Y/%m/%d"), time.strftime("%H:%M:%S"), vis, IR, uvIndex))
    db.commit()
    
    #HUMIDITY SENSOR
    #humidity, temp3 = Adafruit_DHT.read_retry(sensor_hum, pin)
    #print("Humidity = " + str(humidity))
    #print('################################################################')
    
    #add_hum = ("INSERT INTO humidity VALUES(%s,%s,%s)")
    #curs.execute(add_hum, (time.strftime("%Y/%m/%d"), time.strftime("%H:%M:%S"), humidity))
    #db.commit()
    
    time.sleep(10)
    
except KeyboardInterrupt:
  print "\nA keyboard interrupt has been noticed"
  
except:
  print "An error or exception has occurred"
