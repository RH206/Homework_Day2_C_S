#Lesson_2_2. The Greatest Showdown

#Task 1-Write a Python program that prompts the user to enter three numbers. 
# The program should then identify and print out the largest number among the three.

print("To find out what number is the largest of 3 numbers and which is the lowest of the 3 numbers, Enter 3 Numbers now.")

number_1 = int(input('Enter your first number :'))
number_2 = int(input('Enter your second number :'))
number_3 = int(input('Enter your third number :'))
def largest(number_1, number_2, number_3):
    if (number_1 > number_2) and (number_1 > number_3):
        largest_number = number_1
    elif (number_2 > number_1) and (number_2 > number_3):
        largest_number = number_2
    else:
        largest_number = number_3
    print("The largest number is :", largest_number)
def smallest(number_1, number_2, number_3):
    if (number_1 < number_2) and (number_1 < number_3):
        smallest_number = number_1
    elif (number_2 < number_1) and (number_2 < number_3):
        smallest_number = number_2
    else:
        smallest_number = number_3
    print("The smallest number is :", smallest_number)
largest(number_1, number_2, number_3)
smallest(number_1, number_2, number_3)
