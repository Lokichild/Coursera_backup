#Get file
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)

#Create dictionary of hours
hr = dict()
for line in fh:
    if not line.startswith('From '):
        continue
    nwline = line.split()
    time = nwline[5]
    xacttme = time.split(':')
    xact = xacttme[0]
    hr[xact] = hr.get(xact,0) + 1

#Sort dictionary output
lst = list(hr.keys())
lst.sort()
for key in lst:
    print(key, hr[key])