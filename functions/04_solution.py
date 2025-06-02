# Problem: Create a function that returns both the area and circumference of a circle given its radius.

radius=5

def area_circumference(radius):
    area = 3.14 *radius *radius
    circum= 2 *3.14* radius
    return [area,circum]


result=area_circumference(5)
# area, circum=area_circumference(5)
print(type(result))
print( result)

# print( area)
# print( circum)