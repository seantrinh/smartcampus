import time
import datetime
import os
import subprocess

import MySQLdb

db = MySQLdb.connect(
    host = '192.168.1.151',
    user = 'pi',
    passwd = '10416232',
    db = 'wifi',
    port = 3306)

curs = db.cursor()

try:
    while True:
        output = subprocess.check_output("iwconfig wlan0 | grep -i --color bit", shell=True)
        raw_speed = output.split(" ")[11]
        speed = raw_speed.split("=")[1]
        output2 = subprocess.check_output("iwconfig wlan0 | grep -i --color link", shell=True)
        raw_linkquality = output2.split(" ")[11]
        raw_signallevel = output2.split(" ")[14]
        linkquality = raw_linkquality.split("=")[1]
        signallevel = raw_signallevel.split("=")[1]

        print("Bit Rate = " + str(speed) + " Mb/s" + "\n" \
              + "Link Quality = " + str(linkquality) + "\n" \
              + "Signal Level = " + str(signallevel) + " dBM")
        print("-----------------------------")

        add_wifi = ("INSERT INTO wifi VALUES(%s,%s,%s,%s,%s)")
        curs.execute(add_wifi, (time.strftime("%Y/%m/%d"), time.strftime("%H:%M:%S"), speed, linkquality, signallevel))
        db.commit()

        time.sleep(10)

except KeyboardInterrupt:
    print "\nA keyboard interrupt has been noticed"

except:
    print "An error or exception has occurred"
