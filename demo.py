from __future__ import print_function
from __future__ import division

#####

# Power Outage Demo for Kneebone Studios
# Scrape a URL for power outage information
# If number of outages is above a certail threshold, turn off relay on GPIO+

# Jonathan Foote 5/2021

#####


import RPi.GPIO as GPIO
import time
from urllib import urlopen
#from urllib.request import urlopen  # py3
from datetime import datetime
import time
import sys

# python -m pip install beautifulsoup4
# python -m pip install soupsieve
from bs4 import BeautifulSoup



url = "https://poweroutage.us/area/utility/380"
threshold = 350


def get_outage_data(url):
     #print("scraping {}".format(url))
     page = urlopen(url)
     html = page.read().decode("utf-8")
     soup = BeautifulSoup(html, "html.parser")

     text = soup.get_text()

     for line in text.split("\n"):
         if len(line.strip()) > 0:
             words = line.split()
             if len(words) == 3:
                 if words[1] == 'Outages:':
                      try:
                           outages = int(words[2].replace(',',""))
                      except ValueError:
                           return -1
                      return outages
     return 0





RELAY = 18 # BCM 18, GPIO.1 physical pin 12
# Relay is connected NORMALLY CLOSED so gpio.cleanup() leaves it SET.
# set RELAY TRUE to TURN OFF
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY,GPIO.OUT)


# power on on startup
GPIO.output(RELAY,False)


try:
     while True:
          time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
          outages = get_outage_data(url)
          print("{} customer outages: {}".format(time_str, outages))
          if outages > threshold:
               print("above threshold: POWER OFF")
               GPIO.output(RELAY,True)
          else:
               print("below outage threshold of {}".format(threshold))
               GPIO.output(RELAY,False)
          time.sleep(300.0)

except KeyboardInterrupt:
     print("interrupted")

GPIO.cleanup()               # clean up after yourself
exit(0)

