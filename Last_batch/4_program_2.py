# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.
numbers = []

while True: 
    num = input("Input a number: ")
    if not num.isdigit():
        break
    numbers.apphend(int(num))

if numbers: 
    most_common = max(set(numbers), key=numbers.count)
    print(f"\nNumber with the most duplicates: {most_common} (Appeared {numbers.count(most_common)} times)")
else:
    print("\nNo valid numbers entered.")
