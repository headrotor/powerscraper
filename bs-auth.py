import requests
from datetime import datetime
import json
import time
import sys


# store authorization key in local file so we
# don't check it in to github
authkey_file = '/home/pi/gith/powerscraper/authkey.txt'
#authkey_file = 'authkey.txt'
try:
    with open('authkey.txt') as fp:
        authkey = fp.read()
except FileNotFoundError:
    print('authorization key file not found:\ncreate "{}" with api key'.format(authkey_file))
    exit()
authkey = authkey.strip()

# Create JSON API url from authkey. California is stateid=6
#api_url = f"https://poweroutage.us/api/json_v1.6/county?key={authkey}&stateid=6"

# texas is utility 380, PGE is utility 760
#api_url=f"https://poweroutage.us/api/json_v1.6/countybyutility?key={authkey}&utilityid=760"
# example response
#{'CountyByUtilityId': 6727, 'CountyId': 3402, 'UtilityId': 760, 'StateId': 6, '#CountyName': 'Sierra', 'CustomersTracked': 5555, 'CustomersOut': 0, 'LastUpdate#dDateTime': '2022-10-13T17:07:14Z'}

api_url="https://poweroutage.us/api/json_v1.6/countybyutility?key={}&utilityid=380".format(authkey)


response = requests.get(api_url)
# might want to check for response == 200 here but YOLO

# response is a list of dicts, one per county (JSON already parsed!)
counties = []
outages = []
total_outages = 0
for resp_dict in response.json():
    #print(resp_dict)
    # if county_dict['US_County_FIPS'] is not None:
    #     print(county_dict['CountyName'])
    counties.append(resp_dict['CountyName'])    
    outage_int = int(resp_dict['CustomersOut'])
    outages.append(outage_int)
    total_outages += outage_int

for c in counties:
    print(c + ", ", end="")
print("counties")

for o in outages:
    print(str(o) + ", ", end="")
print("outages")

    
text = "Utility Outages: {}".format(total_outages)

for line in text.split("\n"):
    if len(line.strip()) > 0:
        words = line.split()
        if len(words) == 3:
            if words[1] == 'Outages:':

                print("{} {} {}".format(time.time(),
                                        datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                        line.strip()))
                sys.stdout.flush()

