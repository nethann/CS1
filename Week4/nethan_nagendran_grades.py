exam_grades = []
# exam_tracker = 0

# grades_input = input("Enter the exam grades separated by commas: ")
# grades_list = grades_input.split(",")

# for grade in grades_list:
#     exam_grades.append(int(grade))
#     exam_tracker += 1

# print(f'{attendance_list} took the exam')
# print(f'The highest grade was a {max(exam_grades)}')
# print(f'The lowest grade was a {min(exam_grades)}')
# print(f'The lowest grade was a {sum(exam_grades)/exam_tracker}')


day_1_set = set()
day_2_set = set()

day_1_attendance = str(input("Student arrived for day 1: "))
day_2_attendance = str(input("Student arrived for day 2: "))

# Assuming you want to add each student's name separately to the set
for student in day_1_attendance.split(", "):
    day_1_set.add(student)

for student in day_2_attendance.split(", "):
    day_2_set.add(student)

print(day_1_set)

# Check for duplicates (students who attended both days)
duplicates = day_1_set.intersection(day_2_set)
if duplicates:
    print("Duplicate students who attended both days:", duplicates)
else:
    print("No duplicates, all students are unique across both days")