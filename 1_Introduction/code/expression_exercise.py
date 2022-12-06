hrs = input("Enter Hours: ")
rate = input("Enter rate per hour: ")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if h > 40:
    calc = (40 * r) + ((h-40)*(r * 1.5))
else:
    calc =h * r

print('Pay: ', calc)