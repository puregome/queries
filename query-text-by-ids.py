#!/usr/local/bin/python3
# query.py: run a fixed query on a tweet file
# usage: query-text.py [-f]
# note: option -f: read foreign tweets to be excluded from output
# 20200410 erikt(at)xs4all.nl


import csv
import json
import re
import sys


IDSTR = "id_str"


if len(sys.argv) <= 1:
    print("usage: query-text-by-ids file-with-ids.txt < tweet-file.json")
    sys.exit()


def read_ids():
    ids = []
    id_file = sys.argv[1]
    out_file = open(id_file, "r")
    for line in out_file:
        if re.search("[0-9]", line):
            ids.append(line.strip())
    out_file.close()
    return ids


ids = read_ids()
for line in sys.stdin:
    try:
        json_line = json.loads(line)
        id_str = json_line[IDSTR]
        if id_str in ids:
            print(line.strip())
    except: pass
