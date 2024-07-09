from consts import mdms, rules
from classes.student import Student
from utils import get_courses_with_less_seats, remove_students_till_the_first_assigned_to_courses_with_less_seats
import math

def allot_mdms(students: list[Student], computing_mdms: list):
  mdm_allotments = {k:[] for k in mdms.keys()}

  ans = 'Y'
  mdms_with_less_seats = []
  min_student_num = 0
  while ans == 'Y' or ans == 'y':
    # Allot the courses as per the student choices
    make_mdm_allotments(students[min_student_num:], mdm_allotments, computing_mdms, mdms_with_less_seats)

    # Courses with less than minimum number of allowed students
    mdms_with_less_seats = get_courses_with_less_seats(mdm_allotments)

    if len(mdms_with_less_seats):
      print({k:len(v) for k,v in mdm_allotments.items()})
      ans = input("Do you want to remove courses {} and reallot the seats: ".format(mdms_with_less_seats))
      if ans == 'Y' or ans == 'y':
        # Unallot all the coursers that were alloted to the students after the student having least id that was allowted a course that dmdmsn't have enough students
        min_student_num = remove_students_till_the_first_assigned_to_courses_with_less_seats(mdms_with_less_seats, mdm_allotments)
      else:
        break
    else:
      break

  for mdm, mdm_students in mdm_allotments.items():
    mdm_allotments[mdm] = [students[i].roll_no for i in mdm_students]

  return mdm_allotments


def make_mdm_allotments(students: list[Student], mdm_allotments: dict, computing_mdms: list[str], mdms_with_less_seats = []):
  for i,student in enumerate(students):
    for mdm in student.mdm_choices:
      if len(mdm_allotments[mdm]) <= rules['max_students_in_class'] and mdm not in mdms_with_less_seats and mdm not in student.prev_mdms and get_does_mdm_follow_branch_rules(student, mdm, computing_mdms):
        mdm_allotments[mdm].append(i)
        break
      else:
        continue


def get_does_mdm_follow_branch_rules(student: Student, mdm: str, computing_mdms: list[str]):
  if student.department in rules['computing_departments']:
    if mdm in computing_mdms:
      return True if student.total_prev_same_branch_mdms < rules['same_branch_mdms_allowed']['computing'] else False
    else:
      return True if student.total_prev_same_branch_mdms < rules['total_mdms_allowed'] - rules['same_branch_mdms_allowed']['computing'] else False

  else:
    if mdm not in computing_mdms:
      return True if student.total_prev_same_branch_mdms < rules['same_branch_mdms_allowed']['core'] else False
    else:
      return True if student.total_prev_same_branch_mdms < rules['total_mdms_allowed'] - rules['same_branch_mdms_allowed']['core'] else False