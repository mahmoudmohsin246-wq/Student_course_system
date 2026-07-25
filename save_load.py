from student_function import students,Student
from course_function import Course,courses
import json
import csv
def save_students():
    students_json = []
    for student in students:
        students_json.append(student.student)
    with open("C:/Users/Mega Sore/CLionProjects/PythonProject/NTI_project/student.json", "w") as file:
        json.dump(students_json, file, indent=4)
def save_courses():
    courses_json = []
    for course in courses:
        courses_json.append({
            "course name": course.name_course,
            "course id": course.id_course,
            "credit hours": course.credit_hours,
            "students": course.students
        })
    with open("C:/Users/Mega Sore/CLionProjects/PythonProject/NTI_project/course.json", "w") as file:
        json.dump(courses_json, file, indent=4)
def load_students():
    with open("C:/Users/Mega Sore/CLionProjects/PythonProject/NTI_project/student.json", "r") as file:
        data = json.load(file)
    students.clear()
    for student in data:
        s = Student(
            student["Name"],
            student["ID"],
            student["Academic Year"]
        )
        s.courses = student["Courses"]
def load_courses():
    with open("C:/Users/Mega Sore/CLionProjects/PythonProject/NTI_project/course.json", "r") as file:
        data = json.load(file)
    courses.clear()
    for course in data:
        c = Course(
            course["course name"],
            course["course id"],
            course["credit hours"]
        )
        c.students = course["students"]
        courses.append(c)
def load_students_to_csv():
    with open("C:/Users/Mega Sore/CLionProjects/PythonProject/NTI_project/student.json", "r") as file:
        students_to_upload = json.load(file)
        return students_to_upload
def export_to_csv():
    students_to_csv = load_students_to_csv()
    with open("C:/Users/Mega Sore/CLionProjects/PythonProject/NTI_project/report.csv", "w", newline="") as file:
        data = csv.writer(file)
        data.writerow(["Name", "ID", "Academic Year","Courses"])
        for student in students_to_csv:
            data.writerow([
                student["Name"],
                student["ID"],
                student["Academic Year"],
                student["Courses"]
            ])