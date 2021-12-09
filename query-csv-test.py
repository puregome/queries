#/usr/bin/env python3
# query-csv-test.py: extract query (corona OR covid) AND test in field text from csv file at stdin
# usage: gunzip -c file.csv.gz | python3 query-csv-test.py
# 20200525 erikt(at)xs4all.nl

import csv
import re
import sys

TESTQUERY = r'\btest|getest|sneltest|pcr'
TEXT = "text"

csvreader = csv.DictReader(sys.stdin)
csvwriter = csv.DictWriter(sys.stdout,fieldnames=csvreader.fieldnames)
csvwriter.writeheader()
for row in csvreader:
    if re.search(TESTQUERY, row[TEXT], flags=re.IGNORECASE):
        csvwriter.writerow(row)
