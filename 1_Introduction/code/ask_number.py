num = 0
tot = 0.0

while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input. \nEnter either a number or done')
        continue
    #print(fval)
    num = num + 1
    tot = tot + fval

#print('All done')
print(tot, num, tot/num)