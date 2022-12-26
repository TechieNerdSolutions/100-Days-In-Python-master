# numbers = [1, 2, 3, ]
# new_numbers = [n + 1 for n in numbers]
# name = "Racham"
# new_name = [l + "v" for l in name]
#
# new_name = [l for l in name]
# range_list = [num * 2 for num in range(1, 5)]
# new_list = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# name = [nam for nam in new_list if len(new_list) < 5]
# name_list = [name.upper() for nam in new_list if len(new_list) > 5]

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num * num for num in numbers]  # AM [num**2 for num in numbers]
#
# print(squared_numbers)
#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [num for num in numbers if num % 2 == 0]
# print(result)
#
#
# def filereader(file):
#     """Read file and remove newline tag"""
#     with open(file, "r") as file:
#         f_read = file.readlines()
#         f = [int(i.replace("\n", "")) for i in f_read]
#         return f
#
#
# file1 = filereader("file.txt")
# file2 = filereader("file1.txt")
#
# # find duplicates and save to result
# result = [num for num in file1 if num in file2]

# Write your code above 👆

#print(result)

# with open("file1.txt",'r') as file:
#
# data=file.readlines()
#
# list1=[int(number.strip()) for number in data]
# with open("file2.txt",'r') as file:
#
# data=file.readlines()
#
# list2=[int(number.strip()) for number in data]
# if len(list1)>=len(list2):
#
# result=[number for number in list1 if number in list2]
# else:
#
# result=[number for number in list2 if number in list1]
# print(result)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# #split_sentence = sentence.split(" ")
#
# result = {word: len(word) for word in sentence.split()}
#
# print(result)

#
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# # weather_f = {day: weather_c[day] * 9 / 5 + 32 for day in weather_c}
#
# weather_f = {day: weather_c[day] * 9 / 5 + 32 for (day, temp) in weather_c.items()}
# print(weather_f)


# Dictionary comprehension
# new_dict ={new_key: new_value for item in list}
# new_dict ={new_key: new_value for (key,value) in dict.items()}
# new_dict ={new_key: new_value for (key,value) in dict.items() if test}
# import random
# students = {student:random.randint(1, 100) for student in new_list}
# passed_students = {student: score for (student,score) in students.items() if score >= 50}