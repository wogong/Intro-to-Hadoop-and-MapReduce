#!/usr/bin/python 

import sys 

ipTotal = 0
oldKey = None 

# Loop around the data 
# It will be in the format key\tval 
# Where key is the store name, val is the sale amount 
# 
# All the sales for a particular store will be presented, 
# then the key will change and we'll be dealing with the next store 

for line in sys.stdin: 
    data_mapped = line.strip().split("\t") 
    if len(data_mapped) != 1: 
        # Something has gone wrong. Skip this line. 
        continue 

    thisKey = data_mapped[0] 

    if oldKey and oldKey != thisKey: 
        print oldKey, "\t", ipTotal 
        oldKey = thisKey; 
        ipTotal = 0

    oldKey = thisKey 
    ipTotal = ipTotal +1

if oldKey != None: 
    print oldKey, "\t", ipTotal
