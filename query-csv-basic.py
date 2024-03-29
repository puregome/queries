#/usr/bin/env python3
# query-csv-test.py: extract query (corona OR covid) in field text from csv file at stdin
# usage: gunzip -c file.csv.gz | python3 query-csv-basic.py
# 20200525 erikt(at)xs4all.nl

import csv
import re
import sys

QUERY = "corona|covid"
TEXT = "text"

csvreader = csv.DictReader(sys.stdin)
csvwriter = csv.DictWriter(sys.stdout,fieldnames=csvreader.fieldnames)
csvwriter.writeheader()
for row in csvreader:
    if re.search(QUERY, row[TEXT], flags=re.IGNORECASE):
        csvwriter.writerow(row)
