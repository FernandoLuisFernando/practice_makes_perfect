# Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point

value_1 = float(input("input a divident: "))
value_2 = float(input("input a divisor: "))
quotient = value_1 / value_2
print (f"The quotient is{quotient:.1f}. ")