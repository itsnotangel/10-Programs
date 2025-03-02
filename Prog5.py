# Program: QuotientOfTwoNumbers.py
n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))

if n2 == 0:
    print ("Indeterminate")
else:
    result = n1/n2
    print (f"Result: {n1 / n2:.2f}")
