#!/usr/bin/env python
import sys
import string
import re

# --------------------------------------------------------------------------
#This mapper code will input a genchan gennum input file, and move date into 
#  the value field for output
#  
#  Note, this program is written in a simple style and does not full advantage of Python 
#     data structures,but I believe it is more readable
#
#  Note, there is NO error checking of the input, it is assumed to be correct
#     meaning no extra spaces, missing inputs or counts,etc..
#
# See #  see https://docs.python.org/2/tutorial/index.html for details  and python  tutorials
#
# --------------------------------------------------------------------------

tvshow = []
temp = []

for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")  #split line, into key and value, returns a list
    temp.append(key_value)        # storing this in array to reuse in the next stage
    key_in     = key_value[0]   #key is first item in list
    value_in   = key_value[1]   #value is 2nd item 

    #print key_in
    if (value_in) == 'ABC':           #if this entry is filter shows only for 'ABC'
        tvshow.append(key_in)      # get all the ABC Shows and store it in an array
    
for t in temp:                    # open for loop and traverse the rows one by one
    for show in tvshow:           # open another for loop, which will look for only ABC shows
        if t[0] == show:          # if a show matches ABC show
            if t[1].isdigit():    # if the second value has digis, then prin those key values
                           print( '%s\t%s' % (t[0], t[1]) )  #print a string, tab, and string


#Note that Hadoop expects a tab to separate key value
#but this program assumes the input file has a ',' separating key value
