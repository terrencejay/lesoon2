# Write a Python program that prompts the user to input a year. The program should determine if the given year is a leap year or not and then display an appropriate message. 
# Please note that this is the definition of a leap year: 
# Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.

#get input from user
currentyear=int(input("what year is it? "))
#getting nested if statements to make sure multiple conditions are true.
if currentyear % 4 == 0:
    if currentyear % 100 == 0:
        if currentyear % 400 == 0:
            print("True. It is a leap year")
        else:
            print("False. It is not a leap year")
    else:
        print("true. It is a leap year")
else:
    print("false. It isn't a leap year")

