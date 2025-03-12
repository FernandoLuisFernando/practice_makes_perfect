# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function
numbers = []
while True:
    num = input("Enter anything: ")
    if not num.isdigit():
        break
    numbers.append(int(num))
numbers.sort()
print("\nNumbers from lowest to highest: ", numbers if numbers else "No Valid numbers entered. ")