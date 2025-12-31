#User input of score and filtering of incorrect formats.
score = input("Enter Score: ")
try:
    flscore = float(score)
except:
    print('Please input a numeric value.')
    quit()

#Filtering values outside range.
if flscore > 1.0:
    print('Score above accepted value. Please try again.')
    quit()
elif flscore < 0.0:
    print('Negative scores are not allowed.')
    quit()

#Grade determination.
if flscore >= 0.9 :
    print('A')
elif flscore >= 0.8 :
    print('B')
elif flscore >= 0.7 :
    print('C')
elif flscore >= 0.6 :
    print('D')
else:
    print('F')