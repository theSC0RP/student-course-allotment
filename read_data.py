import csv
from consts import fieldnames, bool_fieldnames
from student import Student

def read_student_data():
  students = []
  i = 0
  with open('student_choices.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
      students.append(create_student(row))

  return students
  
def create_student(student_data):
  for k in bool_fieldnames:
    student_data[k] = True if student_data[k]=="YES" else False

  return Student(student_data)
