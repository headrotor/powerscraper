from __future__ import print_function
from __future__ import division
import RPi.GPIO as GPIO
import time




RELAY = 18 # BCM 18, GPIO.1 physical pin 12
# Relay is connected NORMALLY CLOSED so gpio.cleanup() leaves it SET.
# set RELAY TRUE to TURN OFF
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY,GPIO.OUT)

fname = "scraperlog"
threshold = 1000



# power on on startup
GPIO.output(RELAY,False)

# read in file of scraped outage data    
with open(fname,'r') as fh:
     all_lines = fh.readlines()

try:
     for i, line in enumerate(all_lines):
          fields = line.split()
          time_str = fields[2]
          try:
               outages = int(fields[5].replace(',',""))
          except ValueError:
               print("couyld not convert outage value")
          print("{} {}".format(time_str, outages))
          if outages > threshold:
               print("above threshold")
               GPIO.output(RELAY,True)
          else:
               print("below threshold")
               GPIO.output(RELAY,False)
          if i > 10:
               break
          time.sleep(1.0)

except KeyboardInterrupt:
     print("interrupted")

GPIO.cleanup()               # clean up after yourself
exit(0)

