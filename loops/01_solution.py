'''
Problem: Given a list of numbers, count how many are positive.
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

'''


numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count=0
for num in numbers:
    if num >= 0 :
        count+=1
        print(f"numbers is {num} and it is positive and count is {count}")
    elif num<0 :
        print(f"numbers is {num} and it is negative")


print(f"Count of positive no :{count}")