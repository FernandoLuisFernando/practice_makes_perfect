#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

even_counters = 0 
for i in range(10):
 num = int(input(f"Enter a number {i+1: }"))
 if num % 2 == 0:
    even_counters += 1 
print (f"The total even numbers is/are {even_counters}.")
