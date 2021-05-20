from __future__ import print_function
from __future__ import division

fname = "scraperlog"

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

