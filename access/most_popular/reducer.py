#!/usr/bin/python 

import sys 

maxTotal = 0
linksTotal = 0
maxKey = None
oldKey = None 

# Loop around the data 
# It will be in the format key\tval 
# Where key is the store name, val is the sale amount 
# 
# All the sales for a particular store will be presented, 
# then the key will change and we'll be dealing with the next store 

for line in sys.stdin: 
    thisKey = line

    if oldKey and oldKey != thisKey: 
	if linksTotal > maxTotal:
		maxTotal = linksTotal
		maxKey = oldKey
        oldKey = thisKey
        linksTotal = 0

    oldKey = thisKey 
    linksTotal = linksTotal +1

print maxKey, "\t", maxTotal
