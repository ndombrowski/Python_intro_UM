handle = open('../data/regex_sum_1701457.txt')

import re

numlst = list()
counter = 0

for line in handle:
    line = line.rstrip()

    #extract list of numbers
    num = re.findall('[0-9]+', line)
    if len(num) == 0:
        continue

    #add numbers to list
    numlst = numlst + num

#convert to numbers
for i in range(0, len(numlst)):
    numlst[i] = int(numlst[i])

print(sum(numlst))
