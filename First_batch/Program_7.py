# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

total = 0 
for loop in range(10):
    num = int(input(f"Enter a number{loop+1}: "))
    total += num
print(total)