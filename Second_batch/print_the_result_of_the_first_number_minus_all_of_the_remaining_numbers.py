#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.


numbers = []
for loop in range(10):
    num = float(input(f"Enter a number {loop+1}. "))
    numbers.apphend(num)
    for num in numbers[1:]:
        result -= num
print (f"the result is {result}. ")
