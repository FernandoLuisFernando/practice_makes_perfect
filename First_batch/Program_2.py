# Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.
value_1 = int(input("input your first number: "))
value_2 = int(input("input your second number: "))
if value_1 == value_2 and value_2 == value_1:
    print("Values entered are EQUAL. ")
else:
    print("Values entered are NOT EQUAL. ")