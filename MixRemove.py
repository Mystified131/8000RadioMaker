pl = []

infile = open("Zimmer.m3u", "r")

plist = infile.readline()

while plist:
    pl.append(plist.strip())
    plist = infile.readline()

infile.close()

playlist = []

for elem in pl:
    if "mix" not in elem and "Mix" not in elem:
        playlist.append(elem)
        
oustr = "Zimmer.m3u"

outfile = open("temp.txt", "w")

for elem in playlist:
    outfile.write(elem + '\n')

outfile.close()   

outfile = open(oustr, "w")

with open("temp.txt") as f: 
    for line in f: 
        if not line.isspace(): 
            #sys.stdout.write(line)
            outfile.write(line)

outfile.close()