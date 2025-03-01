# Program: ToptalOfTenNumbers.py
total = 0
for i in range(10):
    num = float(input("Enter number " + str(i + 1) + ": ")) 
    total -= num

print("Sum:", total) 