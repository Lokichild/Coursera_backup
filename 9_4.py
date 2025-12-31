# This program identifys email addresses in a list of emails sent to the user.
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)

email = dict()

for line in fh:
    if not line.startswith('From '):
        continue
    nwline = line.split()
    address = nwline[1]
    email[address] = email.get(address,0) + 1

highcount = None
highadd = None
for address,count in email.items():
    if highcount is None or count > highcount:
        highadd = address
        highcount = count
        
print(highadd, highcount)