'''Problem: Check if a password is
"Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

'''

password = input("Please enter your password : ")

if len(password) < 6 :
    print('Your password is weak')
elif len(password) >6 and len(password) <= 10 :
    print('Your password is Medium')
elif len(password) > 10 :
    print('Your password is strong')
else :
    print("Please enter password again")
