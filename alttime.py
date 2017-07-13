#USE THIS ONLY IF ABSOLUTELY NECESSARY

import ntplib
from time import ctime
import time
import sys

try:
        while True:
                c=ntplib.NTPClient()
                response=c.request('us.pool.ntp.org',version=3)
                print(ctime(response.tx_time))
                time.sleep(10)

except KeyboardInterrupt:
        print("\n A keyboard interrupt has been noticed")

except:
        print("An error or exception has occurred")
