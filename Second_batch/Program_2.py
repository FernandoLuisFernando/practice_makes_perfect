#Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

value_1 = int(input("Enter the first integer: "))
value_2 = int(input("Enter the second integer: "))
if value_1 != value_2:
    print("Both numbers are equal.")
else:
    print("Both numbers are NOT equal.")
    