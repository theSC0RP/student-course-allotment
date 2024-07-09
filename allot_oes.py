from consts import open_electives, rules
from classes.student import Student
from utils import get_courses_with_less_seats, remove_students_till_the_first_assigned_to_courses_with_less_seats
import math

def allot_oes(students: list[Student]):
  oe_allotments = {k:[] for k in open_electives.keys()}

  ans = 'Y'
  courses_with_less_seats = []
  min_student_num = 0
  while ans == 'Y' or ans == 'y':
    # Allot the courses as per the student choices
    make_oe_allotments(students[min_student_num:], oe_allotments, courses_with_less_seats)

    # Courses with less than minimum number of allowed students
    courses_with_less_seats = get_courses_with_less_seats(oe_allotments)

    if len(courses_with_less_seats):
      print({k:len(v) for k,v in oe_allotments.items()})
      ans = input("Do you want to remove courses {} and reallot the seats: ".format(courses_with_less_seats))
      if ans == 'Y' or ans == 'y':
        # Unallot all the coursers that were alloted to the students after the student having least id that was allowted a course that doesn't have enough students
        min_student_num = remove_students_till_the_first_assigned_to_courses_with_less_seats(courses_with_less_seats, oe_allotments)
      else:
        break
    else:
      break

  for oe, oe_students in oe_allotments.items():
    oe_allotments[oe] = [students[i].roll_no for i in oe_students]

  return oe_allotments


def make_oe_allotments(students, oe_allotments, disallowed_oes = []):
  for i,student in enumerate(students):
    for oe in student.oe_choices:
      if len(oe_allotments[oe]) <= rules['max_students_in_class'] and oe not in disallowed_oes and oe not in student.prev_oes:
        oe_allotments[oe].append(i)
        break
      else:
        continue


