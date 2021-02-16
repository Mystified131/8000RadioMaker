import os

contents = []

srchstr = 'C:\\Users\\mysti\\Coding\\BFFMaker\\'

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".m3u"):

            contents.append(filepath)

lendict = {}

for elem in contents: 

    pl = []

    infile = open(elem, "r")

    plist = infile.readline()

    while plist:
        pl.append(plist.strip())
        plist = infile.readline()

    lendict[elem] = len(pl)

    infile.close()

print(lendict)