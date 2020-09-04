# 3.3 Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit.
# For the test, enter a score of 0.85.

score = input("Enter a Score between 0.0 and 1.0: ")
try:
    score = float(score)
except:
    print("Error, please enter a numerical value ")
    quit() # quit() is necessary to avoid traceback call in line 20, after print statement within the except is triggered, as score would then still be a string value and not float and hence logical operator would not work on it.
#Out of all the below conditional statement, the first one that amounts to true will be printed and the rest will be skipped. Had we used if rather than elif, there would be multiple print statements. Eg - 0.95 would be true for all the statements had 'if' been used, except the last one
if score > 1.0 or score < 0.0:
    print("Error, please enter a score between 0.0 and 1.0")
elif score >= 0.9:
    print("Grade A")
elif score >= 0.8:
    print("Grade B")
elif score >= 0.7:
    print("Grade C")
elif score >= 0.6:
    print("Grade D")
else:
    print("Grade F")
