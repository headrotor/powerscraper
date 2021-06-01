from __future__ import print_function
from __future__ import division
import time
import sys


### Sausage grinder program to extract county data from scraperlog and turn it into .csv file




def print_csv_line(the_line, header = False):
     # print a comma-sep line of data, ignoring last field

     if header:
          # split on commas because some county names have spaces
          fields = the_line.split(',')

     else:
          # split on whitespace
          fields = the_line.split()
          # remove commas (1000's formatted with commas, grr!)
          fields = [f.replace(',',"") for f in fields]

     # remove trailing spaces and newlines
     fields = [f.strip() for f in fields]
     for i, f in enumerate(fields[:-3]):
          print("{}, ".format(f), end='')
     print("{}".format(fields[-2]))
     # return count of lines printed
     return i + 1

# if this file does not exist, "gunzip countydata.txt.gz"
fname = "countydata.txt"


print("processing")
# read in file of scraped outage data    
with open(fname,'r') as fh:
     all_lines = fh.readlines()

got_header = False
field_count = 0
try:
     # for every line, print time and compare outage with threshold
     for i, line in enumerate(all_lines):
          fields = line.strip().split()
          if not got_header:
               if fields[-1] == 'counties':
                    got_header = True
                    field_count = print_csv_line(line.strip(), header=True)

          elif fields[-1] == 'outages': 
               count = print_csv_line(line)
               if count != field_count:
                    print("whoops, {} fields in line {}, header has {}".format(
                         i, count, field_count))
                    print("terminating before I make a bad .csv file")
                    exit(0)
except KeyboardInterrupt:
     # someone hit CRTL-C, clean up nicely and exit.
     print("interrupted")

exit(0)

