# @ Author Adewunmi Oladele A.K.A Rachamv
# Project 18: Highest Score
# Date: wed oct 26 08:13:10 AM
"""
Highest Score Using for loops
"""
print("********* Highest Score ********")
student_scores = input("Input a list of student scores ").split()
for numbers in range(0, len(student_scores)):
    student_scores[numbers] = int(student_scores[numbers])
print(student_scores)
HIGHEST_SCORE = 0
for score in student_scores:
    if score > HIGHEST_SCORE:
        HIGHEST_SCORE = score
        # print(HIGHEST_SCORE)

print(f"The highest score in the class is: {HIGHEST_SCORE}")
