#1. Decisions at the Crossroad

#Task 1: Code Correction 
# You are provided with a Python script that uses conditional statements 
# to tell if a number is positive, negative, or zero, but it has some errors. Identify and fix them

print("To tell if a number is positive, negative, or zero enter any number now.")

number = int(input('Enter a Number:'))



if number > 0:
    print("The number is positive.")
if number == 0:
    print("The number is zero.")
if number < 0:
    print("The number is negative.")