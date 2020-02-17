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
    x = int(input("Enter the fibonachi number: ")) - 1 
    fib1 = fib2 = 1
    while x > 0:
        fib1, fib2 = fib2, fib1 + fib2
        x = x - 1
    return fib2    

def avOfList(x):
    s = 0
    x = list(map(int, input().split()))
    for i in range(len(x)):
         s = s + x[i]
    return s/len(x)      

def algProg(x, d, n):
    x = int(input("Enter the first number: "))
    d = int(input("Enter the algebraic progression step: "))
    n = int(input("Enter the of desired members of the algebraic progression: "))
    s = ((2 * x + (n - 1) * d) / 2) * n
    return s

def geoProg(x, q, n):
    x = int(input("Enter the first number: "))
    q = int(input("Enter the geometric progression step(not 1): "))
    n = int(input("Enter the of desired members of the geometric progression: "))
    s = (x * (1 - q**n))/(1-q)
    return s
    
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
    print("average of list: ")
    print(avOfList(0), "\n")
    print("sum of algebraic progression: ")
    print(algProg(0, 0, 0), "\n")
    print("sum of geometric progression: ")
    print(geoProg(0, 0, 0), "\n")



out()



