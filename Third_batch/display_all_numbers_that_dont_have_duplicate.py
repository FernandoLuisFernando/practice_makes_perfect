# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

numbers = []
for loop in range(10):
    num = int(input(f"Enter a number {loop+1}: "))
    numbers.append(num)
for num in numbers:
    if numbers.count(num) == 1:
        print(num)

