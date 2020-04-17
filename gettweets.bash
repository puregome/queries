#!/bin/bash
# run: collect rivm-related tweets
# usage: run
# infor started as /data/tmp/rivm/run
# 20200410 erikt(at)xs4all.nl

DATADIR=/data/twitter/

YEAR=2020
MONTH=02
for DAY in {23..29}
do
   for HOUR in {0..23}
   do
      if [ -z "`echo $HOUR|grep ..`" ]; then HOUR=0$HOUR; fi
      FILEIN=$YEAR$MONTH$DAY-$HOUR.out.gz
      FILEOUT=$YEAR$MONTH$DAY-$HOUR.rivm.gz
      gunzip -c $DATADIR$FILEIN | ./query.py | gzip -c > $FILEOUT
   done
done

YEAR=2020
MONTH=03
for DAY in {1..31}
do
   if [ -z "`echo $DAY|grep ..`" ]; then DAY=0$DAY; fi
   for HOUR in {0..23}
   do
      if [ -z "`echo $HOUR|grep ..`" ]; then HOUR=0$HOUR; fi
      FILEIN=$YEAR$MONTH$DAY-$HOUR.out.gz
      FILEOUT=$YEAR$MONTH$DAY-$HOUR.rivm.gz
      gunzip -c $DATADIR$FILEIN | ./query.py | gzip -c > $FILEOUT
   done
done

YEAR=2020
MONTH=04
for DAY in {1..17}
do
   if [ -z "`echo $DAY|grep ..`" ]; then DAY=0$DAY; fi
   for HOUR in {0..23}
   do
      if [ -z "`echo $HOUR|grep ..`" ]; then HOUR=0$HOUR; fi
      FILEIN=$YEAR$MONTH$DAY-$HOUR.out.gz
      FILEOUT=$YEAR$MONTH$DAY-$HOUR.rivm.gz
      gunzip -c $DATADIR$FILEIN | ./query.py | gzip -c > $FILEOUT
   done
done

exit 0
