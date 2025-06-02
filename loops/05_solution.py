'''
Find the First Non-Repeated Character
Problem: Given a string, find the first non-repeated character.

'''

repeated_string ='racecars'
count_for_each_letter=0
for char in range(0,len(repeated_string)):
    for each_letter in range(1,len(repeated_string)):
        if(repeated_string[each_letter] == repeated_string[char]) :
            count_for_each_letter+=1
ni