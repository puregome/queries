#!/usr/local/bin/python3
# query.py: run a fixed query on a tweet file
# usage: query.py
# 20200410 erikt(at)xs4all.nl

import csv
import json
import re
import sys

NL = "nl"
TEXT = "text"
LANG = "lang"
USER = "user"
SCREENNAME = "screen_name"
IDSTR = "id_str"
FULLTEXT = "full_text"
EXTENDEDTWEET = "extended_tweet"
RETWEETEDSTATUS = "retweeted_status"
REPLYIDSTR = "in_reply_to_status_id_str"
VERIFIED = "verified"

def replaceNewlines(text):
    return(re.sub(r"\n",r"\\n",text))

csvwriter = csv.DictWriter(sys.stdout,[IDSTR,REPLYIDSTR,USER,VERIFIED,TEXT])
csvwriter.writeheader()
for line in sys.stdin:
    try:
        jsonLine = json.loads(line)
        lang = jsonLine[LANG]
        if lang == NL:
            idstr = jsonLine[IDSTR]
            text = jsonLine[TEXT]
            user = jsonLine[USER][SCREENNAME]
            if EXTENDEDTWEET in jsonLine and \
               FULLTEXT in jsonLine[EXTENDEDTWEET]:
                text = jsonLine[EXTENDEDTWEET][FULLTEXT]
            if RETWEETEDSTATUS in jsonLine and \
               EXTENDEDTWEET in jsonLine[RETWEETEDSTATUS] and \
               FULLTEXT in jsonLine[RETWEETEDSTATUS][EXTENDEDTWEET]:
                text = jsonLine[RETWEETEDSTATUS][EXTENDEDTWEET][FULLTEXT]
            replyIdstr = jsonLine[REPLYIDSTR]
            if jsonLine[USER][VERIFIED]: verified = "1"
            else: verified = ""
            csvwriter.writerow({IDSTR:idstr,REPLYIDSTR:replyIdstr,USER:user,VERIFIED:verified,TEXT:replaceNewlines(text)})
    except: pass
