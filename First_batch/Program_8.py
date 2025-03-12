# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
odd_counter = 0 
for loop in range(10):
    num = int(input(f"Enter a number{loop+1}: "))
    if num % 2 != 0:
        odd_counter += 1
print(f"Total odd numbers are {odd_counter}. ")

