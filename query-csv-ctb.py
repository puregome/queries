#/usr/bin/env python3
# query-csv-distance.py: extract social distancing tweets from csv file at stdin
# usage: gunzip -c file.csv.gz | python3 query-csv-test.py
# 20200525 erikt(at)xs4all.nl

import csv
import re
import sys

QUERY = r"ctb|qr|toegangsbewij|testbewij|coronapas|vaccinatiepas|vaccinpas|\bcodes\b|2g|3g|1g|apartheid"
TEXT = "text"


csvreader = csv.DictReader(sys.stdin)
csvwriter = csv.DictWriter(sys.stdout,fieldnames=csvreader.fieldnames)
csvwriter.writeheader()
for row in csvreader:
    if re.search(QUERY,row[TEXT],flags=re.IGNORECASE):
           csvwriter.writerow(row)
