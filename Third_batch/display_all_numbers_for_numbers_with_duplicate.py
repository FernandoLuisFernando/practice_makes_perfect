# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

numbers = []
for int  in range(10):
    num = int(input(f"Enter a number{int+1}: "))
    if num not in numbers:
        numbers.append(num)
print("\nNumbers displayed (first occurence only): ")
for num in numbers:
    print(num)