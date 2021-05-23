# powerscraper
Code and docs for Kneebone Studio power switcher project

Obtain Texas utility customer outage data from https://poweroutage.us/area/utility/380, and turn off a relay if outages exceed a threshold. 

`bs/py` -- run this periodically to get power outage data, for example in a crontab:
```
# m h  dom mon dow   command
*/5 * * * * python3 /home/pi/gith/powerscraper/bs.py >> ~/scraperlog 2>&1
```

`bs.py` generates three lines of output per invocation: a comma-separated list of counties, a comma-separated list of outage counts per county, and a line with timestamps (epoch seconds, date, time), the string "Utility Outages:" followed by the number of outages across all counties.


`demo.py` -- Actual live demo, reads total outage  data from URL above, and turns on a raspberry Pi GPIO.1 (physical pin 12) to trigger power cut relay depending on the number of outages. Works on Python 2.7 currently standard on Rpi. `demo.py` takes one argument: an integer threshold value. Outage data is checked every five minutes repeatedly: power is disconnected if the number of outages is above the threshold and reconnected when below.

`canned-demo.py` -- run this to read data from `scraperlog` text file; run `gunzip scraperlog.gz` to uncompress the data. If not running on a Raspberry Pi with GPIO support, use a command-line option like `--dry-run` to ignore the hardware. Works on Python 2 and Python 3. 

