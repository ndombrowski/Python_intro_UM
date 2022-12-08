fname = '../data/mbox-short.txt'
fh = open(fname) 

count = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    mail = line.split()[1]
    count = count + 1
    
    print(mail)

print("There were", count, "lines in the file with From as the first word")
