def computepay(h,r):
    if h > 40:
        calc = (40 * r) + (h-40)*(r * 1.5)
    else:
        calc = h * r
    return calc

#get data
hrs = input('Enter hours: \n')
rate = input('Enter rate: \n')

#convert to float
try:
    hrs_f = float(hrs)
    rate_f = float(rate)
except:
    print('Please, insert a number')
    quit()

#compute pay
p = computepay(hrs_f, rate_f)

print('Pay: ', p)