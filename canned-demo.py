from __future__ import print_function
from __future__ import division
import time
import sys

use_hw = True
if len(sys.argv) > 1:
     use_hw = False
  
if use_hw:
     try:
          import RPi.GPIO as GPIO
     except ImportError:
          print("Needs to be run on a Raspberry Pi to use the hardware.")
          print("Run again with --dry_run to avoid this error")
          exit(1)
     RELAY = 18 # BCM 18, GPIO.1 physical pin 12
     # Relay is connected NORMALLY CLOSED so gpio.cleanup() leaves it SET.
     # set RELAY TRUE to TURN OFF
     GPIO.setmode(GPIO.BCM)
     GPIO.setup(RELAY,GPIO.OUT)

# if this file does not exist, "gunzip scraperlog.gz"
fname = "scraperlog"
# turn off power if threshold is above this number
threshold = 200
# wait this many seconds before getting next line of data
wait_seconds = 1.0



print("Texas outage data scraped from https://poweroutage.us/area/utility/380")


if use_hw:
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
               print("could not convert outage value")
          print("{} customer outages: {}".format(time_str, outages))
          if outages > threshold:
               print("above threshold: POWER OFF")
               if use_hw:
                    GPIO.output(RELAY,True)
          else:
               print("below outage threshold of {}".format(threshold))
               if use_hw:
                    GPIO.output(RELAY,False)
          # for testing, uncomment if you don't want to read the whole file
          #if i > 10:
          #     break

          # wait and get the next line of data
          time.sleep(wait_seconds)

except KeyboardInterrupt:
     print("interrupted")

if use_hw:
     GPIO.cleanup()               # clean up after yourself
exit(0)

