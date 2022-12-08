name = '../data/words.txt'
handle = open(name)

counts = dict()

#create a dictionary to count the words
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word , 0) + 1

bigcount = None
bigword = None

#go through the dictionary counts and identify the item with the most counts
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)