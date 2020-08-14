#/usr/bin/env python3
# query-csv-ghent.py: extract tweets with emojifrom csv file at stdin
# usage: gunzip -c file.csv.gz | python3 query-csv-test.py
# 20200813 erikt(at)xs4all.nl

import csv
import re
import sys

QUERY = "😀|😁|😂|🤣|😃|😄|😅|😆|😉|😊|😋|😎|😍|😘|😗|😙|😚|☺️|🙂|🤗|🤩|🤔|🤨|😐|😑|😶|🙄|😏|😣|😥|😮|🤐|😯|😪|😫|😴|😌|😛|😜|😝|🤤|😒|😓|😔|😕|🙃|🤑|😲|☹️|🙁|😖|😞|😟|😤|😢|😭|😦|😧|😨|😩|🤯|😬|😰|😱|😳|🤪|😵|😡|😠|🤬|😷|🤮"
TEXT = "text"
IDSTR= "id_str"

csvreader = csv.DictReader(sys.stdin)
csvwriter = csv.DictWriter(sys.stdout,fieldnames=[IDSTR])
for row in csvreader:
    if re.search(QUERY,row[TEXT],flags=re.IGNORECASE):
        csvwriter.writerow({IDSTR:row[IDSTR]})
