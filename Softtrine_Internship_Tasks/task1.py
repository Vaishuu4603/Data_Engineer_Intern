# Task 1: User Input and String Manipulation
# 1. Asks the user to enter their full name.
# 2. Converts the name to title case (first letter capitalized for each word).
# 3. Counts and prints the total number of characters (excluding spaces)

f_name=input("Enter your full name: ")
print(f_name)
print("full name after using title case:- ")
print(f_name.title())
print(len(f_name))

print(f_name.replace(" ",""))

# Output:

# Enter your full name: vAishU d wAlUnj
# vAishU d wAlUnj
# full name after using title case:- 
# Vaishu D Walunj
# 15
# total number of characters excluding spaces:- 
# vAishUdwAlUnj