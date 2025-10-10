#week-4
#creat a function to calculate factorial
#Actually function is defined as a reusable block of code designed to perform a specific task.
#Functions are defined using the def keyword followed by the function name, parentheses, and a colon.

#Factorial is defined as a number is the product of all positive integers from the number down to 1
#it's written with an exclamation mark (!)

#code

def factorial(num):
    fact = 1 #starts with 1
    for i in range(1, num + 1): #for loop goes from 1 to num
        fact *= i #multiply fact by i
    return fact

print(factorial(10))

