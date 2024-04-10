#Lesson_2_3. Leap Year Explorer

#Task 1: Leap Year Checker
#Write a Python program that prompts the user to input a year. 
# The program should determine if the given year is a leap year 
# or not and then display an appropriate message. 
# Please note that this is the definition of a leap year: 
# Every year that is exactly divisible by four is a leap year, 
# except for years that are exactly divisible by 100, 
# but these centurial years are leap years if they are exactly divisible by 400.

print("To Find out if any year is a leap year enter the year now.")

year = int(input('Enter The Year :'))


if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))