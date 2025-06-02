'''
4. Reverse a String
Problem: Reverse a string using a loop.

'''
# mayur
string_to_reverse = input("Please provide the string to reverse : ")
index=len(string_to_reverse)
reverse=''
print(index)
for char in range(0,index) :
    # print(f'char is {string_to_reverse[char]}')
    reverse=string_to_reverse[char]+reverse

print(f"Reverse is {reverse}")