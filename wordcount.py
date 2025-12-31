#Get the name of the file and open it
name = input('Enter file:')
handle = open(name, 'r')

# Count word frequency
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

# Find the most common word
bigcount = None
bigword = None
for word,count in counts.item():
    if bigcoun is None or count > bigcount:
        bigcount = word
        bigcount = count

# All done
print(bigword, bigcount)