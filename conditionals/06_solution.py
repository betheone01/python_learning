'''
Transportation Mode Selection
Problem: Choose a mode of transportation based on the distance 
(e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

'''

Distance =int( input('Please provide your mode of transport : '))

if Distance < 3:
    print("You can choose for walk")
elif Distance >= 3 and Distance < 15 :
    print("You can choose for Bike")
elif Distance >= 15 :
    print ("You can choose for Car")