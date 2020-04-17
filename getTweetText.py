#!/usr/bin/env python3
# getTWeetText.py: extract text from tweets in json format
# usage: gunzip -c tweetfiles.gz | python3 getTweetText.py > tweets.txt
# 20200417 erikt(at)xs4all.nl

import json
import re
import sys

TEXT = "text"
FULLTEXT = "full_text"
EXTENDEDTWEET = "extended_tweet"
RETWEETEDSTATUS = "retweeted_status"

def getTweetText(jsonData):
    text = ""
    if TEXT in jsonData: 
        text = jsonData[TEXT]
    if EXTENDEDTWEET in jsonData and \
       FULLTEXT in jsonData[EXTENDEDTWEET]:
        text = jsonData[EXTENDEDTWEET][FULLTEXT]
    if RETWEETEDSTATUS in jsonData and \
       EXTENDEDTWEET in jsonData[RETWEETEDSTATUS] and \
       FULLTEXT in jsonData[RETWEETEDSTATUS][EXTENDEDTWEET]:
        text = jsonData[RETWEETEDSTATUS][EXTENDEDTWEET][FULLTEXT]
    return(text)

for line in sys.stdin:
    jsonData = json.loads(line)
    tweetText = getTweetText(jsonData)
    tweetLine = re.sub("\n"," ",tweetText)
    print(tweetLine)
