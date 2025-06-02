'''
2. Sum of Even Numbers
Problem: Calculate the sum of even numbers up to a given number n.

'''

n=int(input("Please provide the input : "))
sum=0
for num in range(n):
    if(num%2==0):
        print(f"num is {num}")
        sum+=num

print(f'Sum of even numbers is {sum}')
