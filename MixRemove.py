#Here a list of track addresses is made

pl = []

infile = open("Zimmer.m3u", "r")

plist = infile.readline()

while plist:
    pl.append(plist.strip())
    plist = infile.readline()

infile.close()

playlist = []

#If the track from the address does not contain the word, "Mix", it is added to an output list

for elem in pl:
    if "mix" not in elem and "Mix" not in elem:
        playlist.append(elem)
        
oustr = "Zimmer.m3u"

outfile = open("temp.txt", "w")

for elem in playlist:
    outfile.write(elem + '\n')

outfile.close()   

#The output list contains only non-"Mix"-entitled tracks

outfile = open(oustr, "w")

with open("temp.txt") as f: 
    for line in f: 
        if not line.isspace(): 
            #sys.stdout.write(line)
            outfile.write(line)

outfile.close()