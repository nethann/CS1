def manage_student_grades(student_grades, **args):
    for class_student, class_grade in args.items():
        if class_grade == None:  
            student_grades.pop(class_student)
        else:  
            student_grades[class_student] = class_grade
    return student_grades

# Example usage
student_grades = {'Alice': 85, 'Bob': 72, 'Charlie': 90}
updated_grades = manage_student_grades(student_grades, David=78, Emily=93)
updated_grades = manage_student_grades(updated_grades, Bob=80)
updated_grades = manage_student_grades(updated_grades, Charlie=None)
print(updated_grades)


