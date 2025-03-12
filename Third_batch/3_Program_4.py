# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number
lowest = None 

while True:
    num = input("Enter anything")
    if not num.isdigit():
        break
    num = int(num)
    if lowest is None or num < lowest:
        lowest = num 

if lowest is not None:
    print(f"\nThe lowest number entered: {lowest}")