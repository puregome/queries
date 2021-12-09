#!/usr/local/bin/python3
# query.py: run a fixed query on a tweet file
# usage: query-text.py [-f]
# 20200410 erikt(at)xs4all.nl

import csv
import json
import re
import sys

EN = "en"
QUERY = "corona|covid"
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
LOCATION = "location"
DATADIR = "/data/puregome/"


def replaceNewlines(text):
    text = re.sub(r"\r",r"\\r",text)
    text = re.sub(r"\n",r"\\n",text)
    return text


csvwriter = csv.DictWriter(sys.stdout,[IDSTR,REPLYIDSTR,USER,VERIFIED,TEXT,LOCATION],lineterminator="\n")
csvwriter.writeheader()
for line in sys.stdin:
    try:
        jsonLine = json.loads(line)
        lang = jsonLine[LANG]
        if lang == EN:
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
            text = replaceNewlines(text)
            replyIdstr = jsonLine[REPLYIDSTR]
            if jsonLine[USER][VERIFIED]: verified = "1"
            else: verified = ""
            if jsonLine[USER][LOCATION]: location = jsonLine[USER][LOCATION]
            else: location = ""
            location = replaceNewlines(location)
            if re.search(QUERY, text, flags=re.IGNORECASE):
                csvwriter.writerow({IDSTR:idstr,REPLYIDSTR:replyIdstr,USER:user,VERIFIED:verified,TEXT:text.strip(),LOCATION:location})
    except: pass
