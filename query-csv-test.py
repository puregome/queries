#/usr/bin/env python3
# query-csv-test.py: extract query (corona OR covid) AND test in field text from csv file at stdin
# usage: gunzip -c file.csv.gz | python3 query-csv-test.py
# 20200525 erikt(at)xs4all.nl

import csv
import re
import sys

TESTQUERY = r'\btest|getest|sneltest|pcr'
SICKQUERY = r'verkoud|snot|ziek|sympto|griep|koorts|verhoging|pijn|hoest|nie[sz]|klacht|loopneus|benauwd|vermoeid|(verlies|verlo).*(reuk|smaak)|(reuk|smaak).*(verlies|verlo)'
IKQUERY = r'\b(ik|mij|mijn|me|mn|m\'n|zelf|mezelf|mijzelf|i)\b'
JEQUERY = r'\b(je|jij|jou|jouw|jezelf|u|uw|ge|gij|aub)\b'
TEXT = "text"

csvreader = csv.DictReader(sys.stdin)
csvwriter = csv.DictWriter(sys.stdout,fieldnames=csvreader.fieldnames)
csvwriter.writeheader()
for row in csvreader:
    if re.search(TESTQUERY, row[TEXT], flags=re.IGNORECASE) and \
       re.search(SICKQUERY, row[TEXT], flags=re.IGNORECASE) and \
       (re.search(IKQUERY, row[TEXT], flags=re.IGNORECASE) or
        re.search(JEQUERY, row[TEXT], flags=re.IGNORECASE)):
        csvwriter.writerow(row)
