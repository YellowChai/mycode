#!/usr/bin/env python3
## create file object in "r"ead mode
with open("vlanconfig.cfg", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    count =0
    for i in configlist:
        count+=1
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print(f"There are total of {count} lines in the file vlanconfig.cfg")

