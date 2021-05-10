from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime
import time
import sys
url = "http://olympus.realpython.org/profiles/dionysus"
url = "https://poweroutage.us/area/utility/380"


print("scraping {}".format(url))
sys.stdout.flush()
while True:

    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    text = soup.get_text()

    for line in text.split("\n"):
        if len(line.strip()) > 0:
            words = line.split()
            if len(words) == 3:
                if words[1] == 'Outages:':

                    print("{} {}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                          line.strip()))
                    sys.stdout.flush()
    time.sleep(600)
