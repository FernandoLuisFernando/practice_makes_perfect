# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number
numbers = []
while True:
    num = input("Enter a number: ")
    if not num.isdigit():
        break
    numbers.append(int(num))

if numbers:
    print(f"\nHighest number entered: {max(numbers)}")
else:
    print(f"\n no valid numbers entered.")
    