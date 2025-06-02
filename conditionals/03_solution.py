'''Problem: Assign a letter grade based on a student's score:
 A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).'''


score = int(input("Please provide me your score "))

grade =''

if score >=90 and score <=100 :
    grade='A'
elif (score >=80 and score <=89):
    grade='B'
elif (score >60 and score <=69):
    grade='C'
else :
    grade='F'


print('Your grade based on score $',grade)




