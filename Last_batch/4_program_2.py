# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.
while True: 
    num = input("Input a number: ")
    if num.isdigit():
        break
    