name = '../data/mbox-short.txt'
handle = open(name)

senders_dict = dict()

bigcount = None
bigword = None

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue

    #generate a dict of senders
    mail = line.split()[1]
    senders_dict[mail] = senders_dict.get(mail, 0) + 1

    #identify the most prolific committer
    for key, value in senders_dict.items():
        if bigcount is None or value > bigcount:
            bigcount = value
            bigword = key

print(bigword, bigcount)    