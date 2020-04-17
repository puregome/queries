#!/usr/local/bin/python3
# dutch.py: extract tweets written in Dutch from a tweet file
# usage: dutch.py < tweetfile.json
# note: uses Twitter's lang field
# 20200417 erikt(at)xs4all.nl

import json
import re
import sys

LANG = "lang"

for line in sys.stdin:
    lang = ""
    jsonLine = json.loads(line)
    if LANG in jsonLine: lang = jsonLine[LANG]
    if lang == "nl":
        print(line,end="")
