#!/usr/bin/python

import sys 
import re

for line in sys.stdin: 
    data = line.strip().split(" ") 
    if len(data) == 10: 
        ip, identity, username, date, timezone, get, link, http, status, size = data
        print "{0}".format(re.sub('^http://www.the-associates.co.uk','',link)) 
