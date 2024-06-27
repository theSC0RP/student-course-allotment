from consts import open_electives, rules
from student import Student
from utils import get_courses_with_less_seats, remove_students_till_the_first_assigned_to_courses_with_less_seats

def allot_mdms(students: list[Student]):
  mdm_allotments = {k:[] for k in open_electives.keys()}

  ans = 'Y'
  courses_with_less_seats = []
  while ans == 'Y' or ans == 'y':
    # Allot the courses as per the student choices
    make_mdm_allotments(students, mdm_allotments, courses_with_less_seats)

    # Courses with less than minimum number of allowed students
    courses_with_less_seats = get_courses_with_less_seats(mdm_allotments)

    if len(courses_with_less_seats):
      print({k:len(v) for k,v in mdm_allotments.items()})
      ans = input("Do you want to remove courses {} and reallot the seats: ".format(courses_with_less_seats))
      if ans == 'Y' or ans == 'y':
        # Unallot all the coursers that were alloted to the students after the student having least id that was allowted a course that dmdmsn't have enough students
        remove_students_till_the_first_assigned_to_courses_with_less_seats(courses_with_less_seats, mdm_allotments)
      else:
        break
    else:
      break

  for mdm, mdm_students in mdm_allotments.items():
    mdm_allotments[mdm] = [students[i].roll_no for i in mdm_students]

  return mdm_allotments

def make_mdm_allotments(students, mdm_allotments, disallowed_mdms = []):
  for i,student in enumerate(students):
    for mdm in student.mdm_choices:
      if len(mdm_allotments[mdm]) < rules['max_students_in_class'] and mdm not in disallowed_mdms:
        mdm_allotments[mdm].append(i)
        break
      else:
        continue


