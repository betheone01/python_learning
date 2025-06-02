'''
Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. 
(e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

'''

fruit='Banana'
colour=input('Whats the colour of the fruit : ')
colour=colour.lower()

if colour== 'green' :
    print(f" {fruit} is Unripe")
elif colour == 'yellow' :
    print(f'{fruit} is ripe')
else :
    print(f'{fruit} is Overripe')

