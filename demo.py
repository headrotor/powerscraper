from __future__ import print_function
from __future__ import division
import RPi.GPIO as GPIO
import time



fname = "scraperlog"


RELAY = 18 # BCM 18, GPIO.1 physical pin 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY,GPIO.OUT)

try:
     while True:

          GPIO.output(RELAY,True)
          print("high")
          time.sleep(1.0)
          GPIO.output(RELAY,False)
          print("low")
          time.sleep(1.0)
except KeyboardInterrupt:

     GPIO.cleanup()               # clean up after yourself
     print("interrupted")
     exit(0)
    
with open(fname,'r') as fh:
     all_lines = fh.readlines()

for i, line in enumerate(all_lines):
     fields = line.split()
     time_str = fields[2]
     try:
          outages = int(fields[5])
     except ValueError:
          print("couyld not convert outage value")
     print("{} {}".format(time_str, outages))
     if outages > threshold:
          print("above threshold")
     else:
          print("below threshold")
     if i > 10:
          break
exit(0)

