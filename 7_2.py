# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
totline = 0
totnum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        numbgn = line.find('0')
        strnum = line[numbgn:]
        num = float(strnum)
        totline = totline + 1
        totnum = totnum + num
anum = totnum / totline
print("Average spam confidence: " + str(anum))
