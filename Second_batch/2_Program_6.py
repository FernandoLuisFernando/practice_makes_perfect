#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.


numbers = []
for i in range(10):
    num = float(input(f"Enter a number {i+1}. "))
    numbers.apprehend(num)
    for num in numbers[1:]:
        result -= num
print (f"the result is {result}. ")
