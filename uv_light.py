import SI1145.SI1145 as SI1145
import time
import sys

sensor = SI1145.SI1145()

#This code will result in an error. Will have to fix.
##import MySQLdb
##db = MySQLdb.connect(
##    host = '192.168.1.151',
##    user = 'pi',
##    passwd = '10416232',
##    db = 'light',
##    port = 3306)
##
##curs = db.cursor()
#----------------------------------------------------
try:
    while True:
        vis = sensor.readVisible()
        IR = sensor.readIR()
        UV = sensor.readUV()
        uvIndex = UV / 100.0

        vis2 = 'Vis:             ' + str(vis)
        IR2 = 'IR:              ' + str(IR)
        uvIndex2 = 'UV Index:        ' + str(uvIndex)

        print 'Vis:             ' + str(vis)
        print 'IR:              ' + str(IR)
        print 'UV Index:        ' + str(uvIndex) #CHANGE IN DB TO float(4,2)
        print '-----------------------'

##        addLight = ("INSERT INTO light VALUES(%s,%s,%s,%s,%s)")
##
##        data = open("data.txt", "a+")
##
##        curs.execute(addLight, (time.strftime("%Y/%m/%d"), time.strftime("%H:%M:%S"), vis, IR, uvIndex))
##        db.commit()
##
##        data.write(vis2 + "\n" + IR2 + "\n" + uvIndex2 + "\n")
##        data.write('-----------------------' + "\n")
##        data.close()

        time.sleep(10)


except KeyboardInterrupt:
  print "\nA keyboard interrupt has been noticed"
  
except:
    print "An error or exception has occurred"
