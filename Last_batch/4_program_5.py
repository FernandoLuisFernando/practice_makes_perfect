# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

numbers = []

while True:
    num = input("Enter a number: ")
    if not num.isdigit():
        break
    numbers.append(int(num))

if numbers:
    average = sum(numbers) / len(numbers)
    print(F"\nAverage of entered number: {average:.2f}")
else:
    print(F"\nNo valid numbers entered. ")