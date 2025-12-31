#Initial file input
fname = input("Enter file name: ")
fh = open(fname)

#Create empty list
lst = list([])
target = lst


#Split and filter
for line in fh:
    nwline = line.split()
    for i in nwline:
        if not i in lst:
            target = lst.append(i)
            

#Sort and print
target = lst.sort()
print(lst)