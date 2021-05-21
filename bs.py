from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime
import time
import sys
url = "https://poweroutage.us/area/utility/380"

#print("scraping {}".format(url))
#sys.stdout.flush()

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

text = soup.get_text()

table = soup.find("table", { "class" : "table-striped" })

data = []
#table_body = table.find('tbody')

rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    eldata = [ele for ele in cols if ele]
    if len(eldata) == 3:
        data.append(eldata)

print(len(data))
for d in data:
    print("{}, ".format(d[0]),end="")
print(" counties")

for d in data:
    print("{}, ".format(d[2]),end="")

print(" outages")
#for d in data:
#    print("{}, ".format(str(d[2])))

#print(data)

for line in text.split("\n"):
    if len(line.strip()) > 0:
        words = line.split()
        if len(words) == 3:
            if words[1] == 'Outages:':

                print("{} {} {}".format(time.time(),
                                        datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                        line.strip()))
                sys.stdout.flush()

