#/usr/bin/env python3
# query-csv-distance.py: extract social distancing tweets from csv file at stdin
# usage: gunzip -c file.csv.gz | python3 query-csv-test.py
# 20200525 erikt(at)xs4all.nl

import csv
import re
import sys

QUERY1 = r"1[.,]5\s*m"
QUERY21 = r"afstand"
QUERY22 = r"hou"
TEXT = "text"


csvreader = csv.DictReader(sys.stdin)
csvwriter = csv.DictWriter(sys.stdout,fieldnames=csvreader.fieldnames)
csvwriter.writeheader()
for row in csvreader:
    if re.search(QUERY1,row[TEXT],flags=re.IGNORECASE) or \
       (re.search(QUERY21,row[TEXT],flags=re.IGNORECASE) and
        re.search(QUERY22,row[TEXT],flags=re.IGNORECASE)):
           csvwriter.writerow(row)
