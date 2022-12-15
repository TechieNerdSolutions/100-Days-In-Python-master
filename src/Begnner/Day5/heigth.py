# @ Author Adewunmi Oladele A.K.A Rachamv
# Project 19: student heights
# Date: wed oct 26 10:10:10 AM
"""
student heights
"""
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# print(student_heights)


TOTAL_HEIGHT = 0
for height in student_heights:
    TOTAL_HEIGHT += height
print(f"total height = {TOTAL_HEIGHT}")

NUMBER_OF_STUDENTS = 0
for student in student_heights:
    NUMBER_OF_STUDENTS += 1
print(f"number of students = {NUMBER_OF_STUDENTS}")

average_height = round(TOTAL_HEIGHT / NUMBER_OF_STUDENTS)
print(average_height)
