import time
import sys
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
                output = subprocess.check_output("speedtest-cli")
                result = {}
                for row in output.split("\n"):
                        if ': ' in row:
                                key, value = row.split(': ')
                                result[key.strip(' .')] = value.strip()
                raw_download = result['Download']
                raw_upload = result['Upload']
                download, unit = raw_download.split(" ")
                upload, unit2 = raw_upload.split(" ")
                print("Download: " + download + " mbps")
                print("Upload: " + upload + " mbps")
                print("-------------------------------")

                add_wifi=("INSERT INTO wifirecord VALUES(%s,%s,%s,%s)")
                curs.execute(add_wifi, (time.strftime("%Y/%m/%d"), time.strftime("%H:%M:%S"),download,upload))
                db.commit()
                time.sleep(10)

except KeyboardInterrupt:
        print("\nAkeyboard interrupt has been noticed.")

except:
        print("An error or exception has occurred.")
