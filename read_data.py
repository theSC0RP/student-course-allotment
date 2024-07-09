import csv
from consts import fieldnames, bool_fieldnames
from classes.student import Student

def read_student_data(datafile_path: str, computing_mdms: list[str]) -> list[Student]:
  students = []
  i = 0
  with open(datafile_path, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
      students.append(create_student(row, computing_mdms))

  return students
  
def create_student(student_data, computing_mdms: list[str]) -> Student:
  for k in bool_fieldnames:
    student_data[k] = True if student_data[k]=="YES" else False

  return Student(student_data, computing_mdms)
