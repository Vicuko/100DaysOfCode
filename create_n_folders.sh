#!/bin/sh

a=0
while [ "$a" -lt 100 ]
do
   a=`expr $a + 1`
   mkdir Day$a
done