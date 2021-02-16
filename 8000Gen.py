#This code imports the necessary modules.

import random
import os
from collections import defaultdict
import datetime
import shutil
from pathlib import Path

#this code retrieves the date and time from the computer, to create the timestamp

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))
   

#srchstr = "C:\\Users\\mysti\\Media_Files\\Sounds\\OlderSounds"

#srchstr = 'E:\\OriginalAudio\\Songs'

#srchstr = 'C:\\Users\\mysti\\Downloads'

#srchstr = "C:\\Users\\mysti\\Media_Files\\Sounds\\OlderSounds"

srchstr = "Shuffled_Playlist.txt"

content = []

finlst = []

infile = open(srchstr, "r")

plist = infile.readline()

while plist:
    content.append(plist.strip())
    plist = infile.readline()

infile.close()

leng = len(content)

for y in range(50):
 
    trk = random.randrange(leng - 30)

    skip = random.randrange(1, 30)

    adnum = trk + skip

    dreamcrack = random.randrange(9)
    if dreamcrack < 4:
        adnum = random.randrange(1,len(content))

    adstr = content[adnum]

    if adstr not in finlst:

        finlst.append(adstr)

#ctr = len(finlst)

ctr = 25

playlst = []

plytext = []

for x in range(1, (ctr + 1)):
    print("")
    print("Copying")
    elem = finlst[x]
    trk =  str(Path(finlst[x]).stem)
    p = (Path(finlst[x]))
    trkloc = str(p.parts[-2])
    outr = os.path.basename(elem)
    outstr = 'C:\\Users\\mysti\\Coding\\8000RadioMaker\\Audio\\' + str(x) + "_" + str(tim) + "_" + trkloc + "-__" + outr
    outstrb = str(x) + "_" + trkloc + ": " + outr
    shutil.copy(elem, outstr)
    playlst.append(outstrb)
    plytext.append(outstr)

print("")
print(playlst)     

oustr = "8000_Playlist_" + tim + ".m3u"

outfile = open(oustr, "w")

for elem in plytext:
    outfile.write(elem + '\n')

outfile.close()     

oustr2 = "8000_Tracklist_" + tim + ".txt"

outfile = open(oustr2, "w")

for elem in playlst:
    outfile.write(elem + '\n')

outfile.close()  

## THE GHOST OF THE SHADOW ##
