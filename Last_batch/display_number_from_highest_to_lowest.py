# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function
numbers =[]
while True:
    num = input("Enter a number: ")
    if not num.isdigit():
        break
    numbers.append(int(num))
numbers.sort(reverse=True)

print(f"\nNumbers from highest to lowest", numbers if numbers else "not valid numbers entered.")