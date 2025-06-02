'''Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. 
Everyone gets a $2 discount on Wednesday.
'''

# age=int(input("please provide your age : "))
# price=12
# day='wednesday'

# if day == "Wednesday".lower():

#     if age>=18:
#         price=price-2
#         print("You are adult so price to pay is $",price)
#     else :
#         price-=2
#         print("You are child so price to pay is $",price)
# else :
#     if age>=18:
#         price=price
#         print("You are adult so price to pay is $",price)
#     else :
#         price=price
#         print("You are child so price to pay is $",price)


# Advance 

age=int(input("please provide your age : "))
day="Wednesday"

price=12 if age>=18 else 8 

if day =='Wednesday':
    price=price-2
    print("Price you have to pay is $",price)