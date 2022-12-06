score = input("Enter Score: ")

#convert string to float
try:
    score_nr = float(score)
except:
    print("Error, please enter numeric input")
    quit()

#calculate score
if score_nr >= 0.9:
    print("A")
elif score_nr >= 0.8:
    print("B")
elif score_nr >= 0.7:
    print("C")
elif score_nr >= 0.6:
    print("D")
elif score_nr > 0.6:
    print("D")
else:
    print('F')