fhand = open('../data/mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    email = words[1]
    pieces = email.split('@')
    host = pieces[1]
    print(host)