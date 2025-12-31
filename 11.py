# This file pulls numbers that have been randomly inserted into a file, tells you how many there are, and totals them.
import re

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "regex_sum_2323988.txt"
fh = open(fname)

lst = []
fnllst = []

for line in fh:
    line = line.strip()
    tmpnumlst = re.findall('[0-9]+', line)
    if len(tmpnumlst) > 0:
        lst = lst + tmpnumlst
        

for i in range(len(lst)):
    x = lst[i]
    x = int(x)
    fnllst.append(x)

print(len(fnllst))
print(sum(fnllst))