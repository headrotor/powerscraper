# powerscraper
Code and docs for Kneebone Studio power switcher project

Obtain Texas utility customer outage data from https://poweroutage.us/area/utility/380, and turn off a relay if outages exceed a threshold. 

`bs/py` -- run this periodically to get one line of power outage data, for example in a crontab:
```
# m h  dom mon dow   command
*/5 * * * * python3 /home/pi/gith/powerscraper/bs.py >> ~/scraperlog 2>&1
```

`demo.py` -- Actual live demo, scrapes data from URL above, and turns on a raspberry Pi GPIO.1 (physical pin 12) to trigger power cut relay. Works on Python 2.7 currently standard on Rpi.

`canned-demo.py` -- run this to read data from `scraperlog` text file; run `gunzip scraperlog.gz` to uncompress the data. If not running on a Raspberry Pi with GPIO support, use a command-line option like `--dry-run` to ignore the hardware. Works on Python 2 and Python 3. 

