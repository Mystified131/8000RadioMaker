#This code imports the necessary modules.

import random
import os
from collections import defaultdict
import datetime
from subprocess import call

#this code retrieves the date and time from the computer, to create the timestamp

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))
   

contents = []

srchstr = 'C:\\Users\\mysti\\Coding\\8000RadioMaker\\'

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".m3u") and '8000' not in filepath:

            contents.append(filepath)

#sizdict = {}

#for x in range(7):

    #pl = []

    #infile = open(contents[x], "r")

    #plist = infile.readline()

    #while plist:
        #pl.append(plist.strip())
        #plist = infile.readline()

    #infile.close()

    #sizdict[contents[x]] = len(pl)

filst = []

#limlen = sizdict[contents[0]]

limlen = 4000

pl1 = []

elem = contents[0]

infile = open(elem, "r")

plist = infile.readline()

while plist:
    pl1.append(plist.strip())
    plist = infile.readline()

infile.close()

pl2 = []

elem = contents[1]

infile = open(elem, "r")

plist = infile.readline()

while plist:
    pl2.append(plist.strip())
    plist = infile.readline()

infile.close()

pl3 = []

elem = contents[2]

infile = open(elem, "r")

plist = infile.readline()

while plist:
    pl3.append(plist.strip())
    plist = infile.readline()

infile.close()

pl4 = []

elem = contents[3]

infile = open(elem, "r")

plist = infile.readline()

while plist:
    pl4.append(plist.strip())
    plist = infile.readline()

infile.close()

pl5 = []

elem = contents[4]

infile = open(elem, "r")

plist = infile.readline()

while plist:
    pl5.append(plist.strip())
    plist = infile.readline()

infile.close()

pl6 = []

elem = contents[5]

infile = open(elem, "r")

plist = infile.readline()

while plist:
    pl6.append(plist.strip())
    plist = infile.readline()

infile.close()

pl7 = []

elem = contents[6]

infile = open(elem, "r")

plist = infile.readline()

while plist:
    pl7.append(plist.strip())
    plist = infile.readline()

infile.close()

pl8 = []

elem = contents[7]

infile = open(elem, "r")

plist = infile.readline()

while plist:
    pl8.append(plist.strip())
    plist = infile.readline()

infile.close()

pl9 = []

elem = contents[8]

infile = open(elem, "r")

plist = infile.readline()

while plist:
    pl9.append(plist.strip())
    plist = infile.readline()

infile.close()

spl = []

for x in range(limlen):
    try:
        spl.append(pl1[x])
    except:
        print("Overflow.")
    try:
        spl.append(pl2[x])
    except:
        print("Overflow.")
    try:
        spl.append(pl3[x])
    except:
        print("Overflow.")
    try:
        spl.append(pl4[x])
    except:
        print("Overflow.")
    try:
        spl.append(pl5[x])
    except:
        print("Overflow.")
    try:
        spl.append(pl6[x])
    except:
        print("Overflow.")
    try:
        spl.append(pl7[x])
    except:
        print("Overflow.")
    try:
        spl.append(pl8[x])
    except:
        print("Overflow.")
    
oustr = "Shuffled_Playlist.txt"

outfile = open("temp.txt", "w")

for elem in spl:
    outfile.write(elem + '\n')

outfile.close()   

outfile = open(oustr, "w")

with open("temp.txt") as f: 
    for line in f: 
        if not line.isspace(): 
            #sys.stdout.write(line)
            outfile.write(line)

outfile.close()

print("")

prompt = input("Press any key to generate the playlist.")

print("")

call(["python", "8000Gen.py"])

## THE GHOST OF THE SHADOW ##




