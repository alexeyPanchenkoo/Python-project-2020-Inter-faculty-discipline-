#!/usr/bin/env python3
import math
def plus(x, y):
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    return print(x, " + ", y, " = ", x+y)

def minus(x, y):
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    return print(x, " - ", y, " = ", x-y)

def multiply(x, y):
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    return print(x, " * ", y, " = ", x*y)

def divide(x, y):
    x = int(input("Enter the dividend: "))
    y = int(input("Enter the divider: "))
    return print(x, " / ", y, " = ", x/y)

def power(x, y):
    x = int(input("Enter the number: "))
    y = int(input("Enter the power: "))
    return print(x, " ^ ", y, " = ", x**y)

def sqrt(x):
    x = int(input("Enter the number: "))
    sqr = math.sqrt(x)
    return print("Square root of", x, " = ", sqr)

plus(0,0)
minus(0,0)
multiply(0,0)
divide(0,0)
power(0,0)
sqrt(0)




