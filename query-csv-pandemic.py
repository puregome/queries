#/usr/bin/env python3
# query-csv-distance.py: extract social distancing tweets from csv file at stdin
# usage: gunzip -c file.csv.gz | python3 query-csv-test.py
# 20200525 erikt(at)xs4all.nl

import csv
import re
import sys

TOPICQUERY = "corona|covid|huisarts|mondkapje|rivm|blijfthuis|flattenthecurve|houvol"
PANDEMICQUERY = "|".join([TOPICQUERY, r'virus|besmet|ziekenhui|\bic\b|intensive.care|^zorg|vaccin|[^ad]arts|uitbraak|uitbrak|pandemie|ggd|'+
                                      r'mondkapje|quarantaine|\bwho\b|avondklok|variant|verple|sympto|e.golf|mutant|^omt$|umc|hcq|'+
                                      r'hydroxychloroquine|virolo|zkh|oversterfte|patiënt|patient|intensivist|🦠|ivermectin'])
DISTANCEQUERY = "1[.,]5[ -]*m|afstand.*hou|hou.*afstand|anderhalve[ -]*meter"
LOCKDOWNQUERY = "lock.down|lockdown"
VACCINQUERY = "vaccin|ingeënt|ingeent|inent|prik|spuit|bijwerking|-->|💉|pfizer|moderna|astrazeneca|astra|zeneca|novavax|biontech|booster|vax|mrna|inject"
TESTQUERY = r'\btest|getest|sneltest|pcr'
CTBQUERY = r'(ctb|qr|toegangsbewij|testbewij|coronapas|vaccinatiepas|vaccinpas|\bcodes\b|2g|3g|1g|apartheid)'

QUERY = "|".join([PANDEMICQUERY, TESTQUERY, VACCINQUERY, LOCKDOWNQUERY, DISTANCEQUERY, CTBQUERY])
TEXT = "text"


csvreader = csv.DictReader(sys.stdin)
csvwriter = csv.DictWriter(sys.stdout,fieldnames=csvreader.fieldnames)
csvwriter.writeheader()
for row in csvreader:
    if re.search(QUERY,row[TEXT],flags=re.IGNORECASE):
           csvwriter.writerow(row)
