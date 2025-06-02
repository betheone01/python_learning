'''
Problem: Determine if a year is a leap year. 
(Leap years are divisible by 4, but not by 100 unless also divisible by 400).

'''



year = int(input("Please Enter the year to check the leap year "))

if year % 4 == 0 :

    if year % 400 == 0 :
        print(f'{year} is leap year')
    elif year % 100 == 0 :
        print(f'{year} is not leap year ')

