#Setting initial value
largest = None
smallest = None

#program run
while True:
    #Taking values
    num = input("Enter a number: ")
    #Checking for done command
    if num == "done":
        break
    #Filtering for nonsense input
    try:
        fnum = int(num)
    except:
        print('Invalid input')
        continue
    #Setting first values
    if largest is None:
        largest = fnum
    if smallest is None:
        smallest = fnum
    #Finding largest and smallest values
    if fnum > largest:
        largest = fnum
    elif fnum < smallest:
        smallest = fnum

#Output
print("Maximum is", largest)
print("Minimum is", smallest)