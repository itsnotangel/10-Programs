# Program 8: All Odd Numbers Total

odd = 0

for i in range(10):
    num = int(input("Enter number " + str(i+1) + ": "))
    if num % 2 != 0:
        odd += 1

print (odd)
