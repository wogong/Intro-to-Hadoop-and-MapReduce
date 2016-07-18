#!/usr/bin/python

import sys

salesTotal = 0.0
n = 0

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

    thisSale = data_mapped[0]
    salesTotal = salesTotal + float(thisSale)
    n = n+1

print n, "\t", salesTotal
