#nethan nagendran


class EmptyRosterError(Exception):
    pass

class Student:
    def __init__(self, first_name, last_name, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa

    def get_gpa(self):
        return self.gpa

    def get_first(self):
        return self.first_name

    def get_last(self):
        return self.last_name

class Course:
    def __init__(self):
        self.roster = []

    def add_student(self, student):
        self.roster.append(student)

    def course_size(self):
        return len(self.roster)

    def find_student_highest_gpa(self):
        if not self.roster:
            raise EmptyRosterError("Exception: Course Roster is Empty.")
        highest_gpa_student = self.roster[0]  
        for student in self.roster:
            if student.get_gpa() > highest_gpa_student.get_gpa():
                highest_gpa_student = student
        return highest_gpa_student

course = Course()
while True:
    first_name = input("Enter student's first name: ")
    if first_name.lower() == 'stop':
        break
    last_name = input("Enter student's last name: ")
    while True:
        try:
            gpa = float(input("Enter student's GPA: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for GPA.")

    student = Student(first_name, last_name, gpa)
    course.add_student(student)

try:
    print(f"Course Size: {course.course_size()}")
    top_student = course.find_student_highest_gpa()
    print(f"Top Student: {top_student.get_first()} {top_student.get_last()}, GPA: {top_student.get_gpa()}")
except EmptyRosterError as e:
    print(e)

