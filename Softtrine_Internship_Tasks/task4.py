# Task 4: Factorial using Loops and Recursion
# 1. Implement two functions to calculate the factorial of a given number:
# 1.a. One function using a for loop.
# 1.b. Another function using recursion.
# 2. Ask the user for a number and print its factorial using both methods.

#Recursion

def fact(n):
    if (n==1):
        return 1
    return n*fact(n-1)

#Loop

def facts(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    return factorial

x=int(input("Enter Number for Factorial:- "))
print(x)
print("Factorial Using Recursion: ",fact(x))
print("Factorial Using Loop: ",facts(x))

#output: 

# Enter Number for Factorial:- 5
# 5
# Factorial Using Recursion:  120
# Factorial Using Loop:  120