#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

value_1 = float(input("Enter the first number: "))
value_2 = float(input("Enter the second number: "))

smaller_value = min(value_1, value_2)
print(f"The smaller value is {smaller_value}. ")