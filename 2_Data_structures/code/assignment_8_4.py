fname = '../data/romeo.txt'

fh = open(fname)
lst = list()

for line in fh:
    line = line.rstrip()
    words = line.split()
    for element in words:
        if element not in lst:
            lst.append(element)
    
lst.sort()
print(lst)


