# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

value_1 = int(input("input your first value: "))
value_2 = int(input("input your second value: "))
if value_1 > value_2: 
    print(f"{value_1} is greater that {value_2}.")
else:
        print(f"{value_2} is greater that {value_1}.")
