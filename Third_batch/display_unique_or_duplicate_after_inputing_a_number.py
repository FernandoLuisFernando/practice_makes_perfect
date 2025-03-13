# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

numbers = []

while True:
    num = int(input("Enter anything : "))
    if not num.isdigit():
        break

    num = int(num)

    if num in numbers:
        print("duplicate")
    else:
        print("different")
        numbers.append(num)