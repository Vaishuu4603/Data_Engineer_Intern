# Task 3: Basic Math Operations
# 1. Takes two numbers as input from the user and performs: Addition, Subtraction,
# Multiplication, Division
# 2. Display the results for each operation.

a=int(input("enter number for a: "))
b=int(input("enter number for b: "))

print("\n---Addition---")
def sum(a,b):
    return a+b
x=sum(a,b)
print(f"The sum of {a} and {b} is:- ",x)

print("\n---Subtraction---")
def sub(a,b):
    return a-b
x=sub(a,b)
print(f"The sub of {a} and {b} is:- ",x)

print("\n---Multiplication---")
def mult(a,b):
    return a*b
x=mult(a,b)
print(f"The multiplication of {a} and {b} is:- ",x)

print("\n---Division---")
def div(a,b):
    return a/b
x=div(a,b)
print(f"The division of {a} and {b} is:- ",x)


# output:- 

# enter number for a: 5
# enter number for b: 5

# ---Addition---
# The sum of 5 and 5 is:-  10

# ---Subtraction---
# The sub of 5 and 5 is:-  0

# ---Multiplication---
# The multiplication of 5 and 5 is:-  25

# ---Division---
# The division of 5 and 5 is:-  1.0