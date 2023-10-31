import numpy as np

#Basic functions

def add(a,b):
    return float(a)+float(b)

def subtract(a,b):
    return float(a)-float(b)

def multiply(a,b):
    return float(a)*float(b)

def divide(a,b):
    return float(a)/float(b)



#print(add(2,6))
#print(subtract(2,6))
#print(multiply(2,6))
#print(divide(2,6))

#Special functions

def root(a):
    if int(a):
        count = 0
        a2 = a
        for i in range(0,a):
            a2 = a2-(i+1) 
            count = count+1
            if a2 <= 0:
                break
        return count
    return a**0.5

def square(a):
    return multiply(a,a)

def factorial(a):
    fact = 1
    for i in range(1,a+1):
        fact = multiply(fact,i)
    return int(fact)
        
#print(factorial(9))

#print(square(6))
print(root(9))