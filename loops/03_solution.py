'''
3. Multiplication Table Printer
Problem: Print the multiplication table for a given number up to 10,
 but skip the fifth iteration.

'''

number=int(input("Please provide the number for the table : "))

for num in range(0,11):
    print(f'{number} * {num} = {number*num}')