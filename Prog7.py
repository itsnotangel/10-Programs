# Program: SumOfTenNumbers.py
total = 0

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    total += num

print(f"The sum of all numbers is: {total}")
