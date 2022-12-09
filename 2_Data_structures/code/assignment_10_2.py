name = input('Enter file: ')

if len(name) < 1:
    name = '../data/mbox-short.txt'

handle = open(name)
counts = dict()
lst = list()

for line in handle:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    
    #extract hour
    time = line.split()[5]
    hour = time.split(':')[0]

    #make dict of hours
    counts[hour] = counts.get(hour, 0) + 1

#convert to sorted list
for key, value in counts.items():
    lst.append((key, value))

#sort list
lst = sorted(lst, reverse = False)

#print one result per line
for key, value in lst:
    print(key, value)