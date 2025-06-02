'''
Problem: Suggest an activity based on the weather 
(e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

'''

weather = input("Please provide the weather to recommend the activity : ")


if weather.lower() == 'sunny':
    print("Go for a walk")
elif weather.lower() == 'rainy':
    print("Read a book")
elif weather.lower()== 'snowy' :
    print("Build a snowman")
else :
    print("Do something productive")
