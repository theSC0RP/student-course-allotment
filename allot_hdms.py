from consts import honors, double_minors, rules, departments_courses, departments
from classes.student import Student
from utils import get_courses_with_less_seats, remove_students_till_the_first_assigned_to_courses_with_less_seats, get_hdm_studnets
import re

def allot_hdms(students: list[Student]):
  department_wise_allowed_hdms = get_department_wise_allowed_hdms()


  students_for_hdm = get_hdm_studnets(students)
  print("Total HDM students: {}".format(len(students_for_hdm)))
  

  honor_allotments = {k:[] for k in honors.keys()}
  dm_allotments = {k:[] for k in double_minors.keys()}

  ans = 'Y'
  courses_with_less_seats = []
  min_student_num = 0
  while ans == 'Y' or ans == 'y':
    # Allot the courses as per the student choices
    make_hdm_allotments(students_for_hdm[min_student_num:], department_wise_allowed_hdms, honor_allotments, dm_allotments, courses_with_less_seats)

    # Courses with less than minimum number of allowed students
    courses_with_less_seats = get_courses_with_less_seats(honor_allotments) + get_courses_with_less_seats(dm_allotments)


    if len(courses_with_less_seats):
      print("\nHonors: ", {k:len(v) for k,v in honor_allotments.items()})
      print("Double Minors: ", {k:len(v) for k,v in dm_allotments.items()})

      total_students = 0
      for k,v in honor_allotments.items():
        total_students += len(v)
      for k,v in dm_allotments.items():
        total_students += len(v)
      print("Total Students: ", total_students)

      
      ans = input("\nDo you want to remove courses {} and reallot the seats: ".format(courses_with_less_seats))
      if ans == 'Y' or ans == 'y':
        # Unallot all the coursers that were alloted to the students after the student having least id that was allowted a course that dhdmsn't have enough students
        allotments_combined = {}
        allotments_combined.update(dm_allotments)
        allotments_combined.update(honor_allotments)
        min_student_num = remove_students_till_the_first_assigned_to_courses_with_less_seats(courses_with_less_seats, allotments_combined)

        honor_allotments = {k:v for k, v in allotments_combined.items() if re.match(r"H\d+", k)}
        dm_allotments = {k:v for k, v in allotments_combined.items() if re.match(r"DM\d+", k)}
      else:
        break
    else:
      break

  for honor, honor_students in honor_allotments.items():
    honor_allotments[honor] = [students_for_hdm[i].roll_no for i in honor_students]

  for dm, dm_students in dm_allotments.items():
    dm_allotments[dm] = [students_for_hdm[i].roll_no for i in dm_students]

  return honor_allotments, dm_allotments

def make_hdm_allotments(students, department_wise_allowed_hdms, honor_allotments, dm_allotments, disallowed_hdms = []):
  for d in department_wise_allowed_hdms.keys():
    department_wise_allowed_hdms[d] = list(set(department_wise_allowed_hdms[d]) - set(disallowed_hdms))
    
  for i,student in enumerate(students):
    department = student.department

    for hdm in student.hdm_choices:
      if hdm in department_wise_allowed_hdms[department]:
        if re.match(r"DM\d+", hdm) and len(dm_allotments[hdm]) <= rules['max_students_in_class']:
          dm_allotments[hdm].append(i)
          break
        elif re.match(r"H\d+", hdm) and len(honor_allotments[hdm]) <= rules['max_students_in_class']:
          honor_allotments[hdm].append(i)
          break



def get_department_wise_allowed_hdms():
  department_wise_allowed_hdms = {}
    
  computing_dms = []
  computing_honors = []
  for cd in rules["computing_departments"]:
    computing_dms.extend(departments_courses[cd]["DM"])
    computing_honors.extend(departments_courses[cd]["HONORS"])


  all_dms = []
  for d in departments.keys():
    all_dms.extend(departments_courses[d]["DM"])

  for d in departments.keys():
    if d in rules["computing_departments"]:
      honors = computing_honors
      dms = list(set(all_dms) - set(computing_dms))
    else:
      honors = departments_courses[d]['HONORS']
      dms = list(set(all_dms) - set(departments_courses[d]['DM']))
      
    # department_wise_allowed_hdms[d]['HONORS'] = honors
    # department_wise_allowed_hdms[d]['DM'] = dms
    department_wise_allowed_hdms[d] = honors + dms

  return department_wise_allowed_hdms
