import os

#This code checks the dirctory for .m3u files and adds them to a list

contents = []

srchstr = 'C:\\Users\\mysti\\Coding\\BFFMaker\\'

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".m3u"):

            contents.append(filepath)

#This code sets up a dictionary with addresses and their place in as dictionary values

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

#Thos code prints the results

print(lendict)