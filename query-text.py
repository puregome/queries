#!/usr/local/bin/python3
# query.py: run a fixed query on a tweet file
# usage: query-text.py [-f]
# note: option -f: read foreign tweets to be excluded from output
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
DATADIR = "/data/puregome/"
FOREIGNFILE = "FOREIGN"

def readForeignTweets():
    foreignTweets = {}
    try:
        inFile = open(DATADIR+FOREIGNFILE,"r")
        for line in inFile:
            foreignTweets[line.strip()] = True
        inFile.close()
    except: pass
    return(foreignTweets)

def replaceNewlines(text):
    text = re.sub(r"\r",r"\\r",text)
    text = re.sub(r"\n",r"\\n",text)
    return(text)

if len(sys.argv) > 1: foreignTweets = readForeignTweets()
else: foreignTweets = {}

csvwriter = csv.DictWriter(sys.stdout,[IDSTR,REPLYIDSTR,USER,VERIFIED,TEXT],lineterminator="\n")
csvwriter.writeheader()
for line in sys.stdin:
    #try:
    if True:
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
            text = replaceNewlines(text)
            replyIdstr = jsonLine[REPLYIDSTR]
            if jsonLine[USER][VERIFIED]: verified = "1"
            else: verified = ""
            if not text in foreignTweets:
                csvwriter.writerow({IDSTR:idstr,REPLYIDSTR:replyIdstr,USER:user,VERIFIED:verified,TEXT:text.strip()})
    #except: pass
