#!/usr/local/bin/python3
# query-text-retweet.py: extract retweet information from json file
# usage: query-text-retweet.py < file
# note: adapted from quert-text.py
# 20220103 erikt(at)xs4all.nl

import csv
import json
import re
import sys

NL = "nl"
LANG = "lang"
IDSTR = "id_str"
USER = "user"
SCREENNAME = "screen_name"
DATE = "created_at"
RETWEETED_STATUS = "retweeted_status"
RETWEETED_IDSTR = "retweeted_" + IDSTR
RETWEETED_USER = "retweeted_" + USER
RETWEETED_DATE = "retweeted_" + DATE


csvwriter = csv.DictWriter(sys.stdout,
        [IDSTR, USER, DATE, RETWEETED_IDSTR, RETWEETED_USER, RETWEETED_DATE ], lineterminator="\n")
csvwriter.writeheader()
for line in sys.stdin:
    try:
        jsonLine = json.loads(line)
        lang = jsonLine[LANG]
        if lang == NL and RETWEETED_STATUS in jsonLine:
            idstr = jsonLine[IDSTR]
            user = jsonLine[USER][SCREENNAME]
            date = jsonLine[DATE]
            retweeted_idstr = jsonLine[RETWEETED_STATUS][IDSTR]
            retweeted_user = jsonLine[RETWEETED_STATUS][USER][SCREENNAME]
            retweeted_date = jsonLine[RETWEETED_STATUS][DATE]
            csvwriter.writerow({ IDSTR: idstr, USER: user, DATE: date,
                RETWEETED_IDSTR: retweeted_idstr, 
                RETWEETED_USER: retweeted_user, 
                RETWEETED_DATE: retweeted_date })
    except: pass
