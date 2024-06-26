"""
import sys
num1 = sys.argv[1]
num2 = sys.argv[2]
sum_of_nos = (num1+num2)
print(sum_of_nos)
"""
"""
# Simple Arithmetic: Write a Python program to add two numbers provided by the user.
num1 = int(input("enter first number:"  ))
num2 = int(input("enter second number:" ))
print(num1 + num2)
"""
"""
# Odd or Even: Write a Python program that checks if a number entered by the user is odd or even.
num1 = int(input("enter any number: "))
if num1 % 2 == 0:
    print("num1 is even")
else:
    print("num1 is odd")
"""
"""
# Sum of Natural Numbers: Write a Python program to find the sum of all natural numbers up to a given number.
n = int(input("Enter a number: "))
sum_n = sum(range(1, n + 1))
print("The sum is:", sum_n)
"""
"""
# Write a Python program to calculate the factorial of a number provided by the user.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("The factorial is:", factorial(num))
"""
# Fibonacci Sequence: Write a Python program to generate the Fibonacci sequence up to n terms.  
num = int(input("enter any number: "))
a , b = 0 , 1
fibonnaci_series = []

for i in range(num):
    fibonnaci_series.append(a)
    a,b = b, a+b
print(fibonnaci_series)

