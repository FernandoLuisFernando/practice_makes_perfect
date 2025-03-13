#Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

Dividend = float(input("Enter your first value: "))
Divisor = float(input("Enter your second value: "))
if Divisor == 0:
    print("Error: try another number.")
quotient_result = Dividend / Divisor
print(f"The answer is {quotient_result:.0f}. ")


