#/usr/bin/env python3
# query-csv-distance.py: extract social distancing tweets from csv file at stdin
# usage: gunzip -c file.csv.gz | python3 query-csv-test.py
# 20200525 erikt(at)xs4all.nl

import csv
import re
import sys

QUERY1 = r"1[.,]5[ -]m"
QUERY2 = r"afstand.*hou|hou.*afstand"
QUERY3 = r"anderhalve[ -]*meter"
TEXT = "text"


csvreader = csv.DictReader(sys.stdin)
csvwriter = csv.DictWriter(sys.stdout,fieldnames=csvreader.fieldnames)
csvwriter.writeheader()
for row in csvreader:
    if re.search(QUERY1,row[TEXT],flags=re.IGNORECASE) or \
       re.search(QUERY2,row[TEXT],flags=re.IGNORECASE) or \
       re.search(QUERY3,row[TEXT],flags=re.IGNORECASE):
           csvwriter.writerow(row)
