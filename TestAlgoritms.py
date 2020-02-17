#!/usr/bin/env python3
import math
def plus(x, y):
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    return x+y #print(x, " + ", y, " = ", x+y)

def minus(x, y):
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    return x-y #print(x, " - ", y, " = ", x-y)

def multiply(x, y):
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    return x*y #print(x, " * ", y, " = ", x*y)

def divide(x, y):
    x = int(input("Enter the dividend: "))
    y = int(input("Enter the divider: "))
    return x/y #print(x, " / ", y, " = ", x/y)

def power(x, y):
    x = int(input("Enter the number: "))
    y = int(input("Enter the power: "))
    return x**y #print(x, " ^ ", y, " = ", x**y)

def sqrt(x):
    x = int(input("Enter the number: "))
    return math.sqrt(x) #print("Square root of", x, " = ", sqr)

def fact(x):
    x = int(input("Enter the number: "))
    s = 1     
    while x > 0:
        s = s * x
        x = x - 1
    return s   
def fib(x):
    x = int(input("Enter the fibonachi number: ")) 
    fib1 = fib2 = 1
    while x > 0:
        fib1, fib2 = fib2, fib1 + fib2
        x = x - 1
    return fib2    

def out():
    print("plus: ")
    print( plus(0,0), "\n")
    print("minus: ")
    print(minus(0,0), "\n")
    print("multiply: ")
    print(multiply(0,0), "\n")
    print("divide: ")
    print(divide(0,0), "\n")
    print("power: ")
    print(power(0,0), "\n")
    print("square root: ")
    print(sqrt(0), "\n")
    print("factorial:")
    print(fact(0), "\n")
    print("fibonachi: ")
    print(fib(0), "\n")
out()



