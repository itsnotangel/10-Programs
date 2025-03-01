odd = 0

for i in range(10):
    num = float(input("Enter number " + str(i+1) + ": "))
    if i % 2 != 0:
        odd += 1

print ("Number of odd numbers: " , odd)